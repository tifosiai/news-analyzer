import sys
import csv
from sqlalchemy import create_engine, text
from utils import load_pos_model
from stemming import stem_sentence

# Set the console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Replace these with your actual database credentials
dbname = 'stemming_db'
user = 'postgres'
password = 'AdaCedar1'
host = '207.180.220.208'
port = '5432'

# Define the SQLAlchemy engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Specify the CSV file path
csv_file_path = 'testing_stemmer.csv'

# Loading the model
model, w2i, idx2tag = load_pos_model()
print("PoS model is loaded.")

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Index', 'Original Sentence', 'Stemmed Sentence (new version)', 'Stemmed Sentence (latest version)', 'Predicted Sentence', 'Table'])

    # Variables to calculate total accuracy for stemmed sentence
    total_stemmed_words = 0
    correct_stemmed_words = 0

    # Variables to calculate total accuracy for stemOld
    total_stemOld_words = 0
    correct_stemOld_words = 0

    # Lists to store indexes of inaccurate stemmed sentences and stemmed (old) sentences
    inaccurate_stemmed_info = []
    inaccurate_stemOld_info = []

    # Variables to maintain the running count of sentences across all tables
    total_sentences_processed = 0

    print("The sentences are in the process of loading.")

    # Process each table
    for table in ['labeling_feray', 'labeling_gunel', 'labeling_fuad']:
        # Connect to the database using the engine
        with engine.connect() as connection:
            # Build a SELECT statement with conditions and order by ID in ascending order
            query = text(f"SELECT original_sentence, predicted_sentence, last_version_output FROM {table} WHERE done = 'TRUE' AND last_version_output IS NOT NULL")

            # Execute the query
            result = connection.execute(query)

            # Fetch the results
            rows = result.fetchall()

            # Process the results for the current table
            for index, row in enumerate(rows, start=1):
                original_sentence = row[0]  # Assuming the original_sentence is in the first column
                predicted_sentence = row[1]  # Assuming the predicted_sentence is in the second column
                last_version_output = row[2]  # Assuming the last_version_output is in the third column

                # Increment the total sentences processed count
                total_sentences_processed += 1

                # Calculate the index relative to all tables
                absolute_index = total_sentences_processed

                # Split the original sentence into words
                words_original = original_sentence.split()

                # Apply stemming to each word
                stemmed_words = stem_sentence(original_sentence, model, w2i, idx2tag, return_list=True)
                # Join the stemmed words back into a sentence
                stemmed_sentence = ' '.join(stemmed_words)

                # Count the number of correct words for stemmed sentence
                correct_stemmed_words += sum(1 for stem, pred in zip(stemmed_words, predicted_sentence.split()) if stem == pred)

                # Update the total number of words for stemmed sentence
                total_stemmed_words += len(stemmed_words)

                # Count the number of correct words for last version output (Stemmed Sentence (old))
                if last_version_output is not None:
                    correct_stemOld_words += sum(1 for word in last_version_output.split() if word in predicted_sentence.split())

                    # Update the total number of words for last version output (Stemmed Sentence (old))
                    total_stemOld_words += len(last_version_output.split())

                # Check if accuracy is not equal to 100% for stemmed sentences
                if stemmed_sentence != predicted_sentence:
                    inaccurate_stemmed_info.append((absolute_index))

                # Check if accuracy is not equal to 100% for stemmed (old) sentences
                if last_version_output is not None and last_version_output != predicted_sentence:
                    inaccurate_stemOld_info.append((absolute_index))

                # Write the row to the CSV file with the table name
                csv_writer.writerow([absolute_index, original_sentence, stemmed_sentence, last_version_output, predicted_sentence, table])

print("The process of loading the sentences is complete.")

# Convert inaccurate_stemmed_info and inaccurate_stemOld_info into sets
inaccurate_stemmed_set = set(inaccurate_stemmed_info)
inaccurate_stemOld_set = set(inaccurate_stemOld_info)

acc_increased = inaccurate_stemOld_set - inaccurate_stemmed_set
acc_dropped = inaccurate_stemmed_set - inaccurate_stemOld_set
intersection_set = inaccurate_stemmed_set & inaccurate_stemOld_set

# Create a set to store indexes that need to be removed from intersection_set
indexes_to_remove = set()

# Loop through the intersection_set
for index in intersection_set:
    corresponding_row = None
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if int(row[0]) == index:
                corresponding_row = row
                break

    if corresponding_row:
        # Calculate accuracy levels for this specific index
        stemmed_old_accuracy = sum(1 for word in corresponding_row[3].split() if word in corresponding_row[4].split()) / len(corresponding_row[4].split()) * 100
        stemmed_new_accuracy = sum(1 for stem, pred in zip(corresponding_row[2].split(), corresponding_row[4].split()) if stem == pred) / len(corresponding_row[4].split()) * 100

        if stemmed_new_accuracy > stemmed_old_accuracy:
            acc_increased.add(index)
            indexes_to_remove.add(index)
        elif stemmed_old_accuracy > stemmed_new_accuracy:
            acc_dropped.add(index)
            indexes_to_remove.add(index)

# Remove the indexes from intersection_set
intersection_set -= indexes_to_remove

if acc_dropped:
    print("accuracy dropped in the following indices:")
    print(acc_dropped)

if acc_increased:
    print("\naccuracy increased in the following indices:")
    print(acc_increased)

if intersection_set:
    print("\naccuracy stays the same in the following indices:")
    print(intersection_set)

# Calculate average accuracy for stemmed sentence
average_stemmed_accuracy = (correct_stemmed_words / total_stemmed_words) * 100 if total_stemmed_words > 0 else 0
print(f"\navg accuracy for new version: {average_stemmed_accuracy:.2f}%")

# Calculate average accuracy for last version output (Stemmed Sentence (old))
average_stemOld_accuracy = (correct_stemOld_words / total_stemOld_words) * 100 if total_stemOld_words > 0 else 0
print(f"\navg accuracy for last version: {average_stemOld_accuracy:.2f}%")

# User input section
user_input_index = int(input("\nEnter the index of the sentence to display (0 to exit): "))
while user_input_index != 0:
    corresponding_row = None
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if int(row[0]) == user_input_index:
                corresponding_row = row
                break

    if corresponding_row:
        print("\nOriginal Sentence:", corresponding_row[1])
        print("Stemmed Sentence (new version):", corresponding_row[2])  
        print("\nStemmed Sentence (latest version):", corresponding_row[3])
        print("\nPredicted Sentence:", corresponding_row[4])
        print("\nTable:", corresponding_row[5])


        # Calculate accuracy levels for this specific index
        stemmed_old_accuracy = sum(1 for word in corresponding_row[3].split() if word in corresponding_row[4].split()) / len(corresponding_row[4].split()) * 100
        stemmed_new_accuracy = sum(1 for stem, pred in zip(corresponding_row[2].split(), corresponding_row[4].split()) if stem == pred) / len(corresponding_row[4].split()) * 100

        print(f"\nthe accuracy for last version: {stemmed_old_accuracy:.2f}%")
        print(f"\nthe accuracy for new version: {stemmed_new_accuracy:.2f}%")
    else:
        print("No data found for the specified index.")

    user_input_index = int(input("\nEnter the index of the sentence to display (0 to exit): "))