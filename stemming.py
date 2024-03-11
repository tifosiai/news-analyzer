from grammatical_rules import ğ_to_q, y_to_k, reinstate_vowel
from utils import uppercase, load_allwords, load_verb, load_locations, load_names, remove_punctuations, \
                  load_auxiliary, load_exceptions, maq_mek, lar_ler, load_surnames, pos_tag_predict, load_pronoun
import re


# Load the all words in Azerbaijani language in stemmed format
allwords = load_allwords()
# Load all verbs in the stemmed format
verbs = load_verb()
# Load all geographical locations 
locations = load_locations()
# Load names
names = load_names()
names_gil = [name + "gil" for name in names]
# Load pronoun
pronoun = load_pronoun()
# Load surnames
surnames = load_surnames()
# Load auxiliary part of speech tags that are not "omonim" with other part of speech tags
auxiliary = load_auxiliary()
# Load the exception nouns list that lose their vowel while adding mənsubiyyət, təsirlik, yönlük, yiyəlik suffixes
exception_nouns = load_exceptions()

# Exception list that are already in their stem format and are not in the word list
exception_list = {'da', 'də', 'ya', 'adə', 'ha', 'əşşi', "ax"}


# Lexical suffixes that need to stay after the hyphen
lexical_suffix = {'cı', 'ci', 'cu', 'cü', 'dakı', 'dəki', 'lıq', 'lik', 'luq', 'lük'}

# Mənsubiyyət, yiyə lik, yönlük, təsirlik suffixes set
mensubiyyet_hal = {'ın', 'in', 'un', 'ün', 'n', 'ım', 'im', 'um', 'üm',
                    'ımız', 'imiz', 'umuz', 'ümüz', 'mız', 'miz', 'muz', 'müz',
                    'ınız', 'iniz', 'unuz', 'ünüz', 'nız', 'niz', 'nuz', 'nüz',
                    'ı', 'i', 'ü', 'u', 'm', 'sı', 'si', 'su', 'sü', 'nın', 'nin', 'nun', 'nün'
                    'a', 'ə', 'ya', 'yə', 'nı', 'ni', 'nü', 'nu'}

#Yerlik suffixes set
yerlik_hal = {'da','də'}

pos_tag_to_wordlist = {
    "Feil": verbs,
    "Əvəzlik": pronoun,
}

def stem_sentence(sentence: str, model, w2i, idx2tag, return_list=False) -> str:
    """
    The function is responsible to return the stemmed version of given sentence
    Args:
        sentence: The given sentence that will be stemmed
        model: The POS model (load_the_pos_model() should be called for this parameter)
        w2i: Word to index (load_the_pos_model() should be called for this parameter)
        idx2tag: Index to tag (load_the_pos_model() should be called for this parameter)
        return_list: Return as a list

    Returns:
        The stemmed version of given sentence as string format
    """
    # Finding the POS of each word
    pos_tags_of_sentence = pos_tag_predict(sentence, model, w2i, idx2tag)

    # Stemmed sentence list
    stemmed_sentence_list = [stemmer(surname_stem(remove_punctuations(word_and_pos['word']), model, w2i, idx2tag), word_and_pos['label'])
                             for word_and_pos in pos_tags_of_sentence]
    if return_list:
        return stemmed_sentence_list
    return " ".join(stemmed_sentence_list)



def stemmer(word: str, pos_tag: str) -> str:

    first_letter = False
    if word != "":
        first_letter = word[0].isupper()
    # If the first letter is upper search the word in names list as well
    if first_letter:
        wordlist = {*allwords, *names, *locations,*surnames, *names_gil}  # Concatenating sets
    else:
        wordlist = allwords
    """
    This function returns the stem of the given word with respect to Azerbaijani language grammatical rules.
    The function does not lowercase the word, thus preserves case format.
    The input word has to be pre-processed(punctuations has to be removed) before giving it to the function.

    Args:
        word: The given word in a string format.
        pos_tag: POS tag of the given word


    Returns:
        The stem of the given word.
    """

    for key in pos_tag_to_wordlist:
        if key in pos_tag:
            wordlist = pos_tag_to_wordlist[key]
            break 
    
    if word.replace('I', 'ı').replace('İ', 'i').lower() not in allwords:
        if '-' in word:
            parts = word.split('-')
            second_last_part = parts[-2].replace('.', '', 1).replace(',', '').replace(':', '')
            if second_last_part.isdigit() and not parts[-1].isnumeric() and parts[-1] not in lexical_suffix:
                return '-'.join(parts[:-1])
            elif not any(part.isdigit() for part in parts) and second_last_part not in lexical_suffix:
                if parts[-1] in yerlik_hal or parts[-1] in mensubiyyet_hal:
                    return parts[0]  # Return the first part if the second part is in yerlik_suffix
                else:
                    return word  # Return the original word if the condition is not met

    # Knowing whether the first letter is upper or not

    # Boolean list shows whether each letter of the word is upper-cased or not
    is_uppercase = [letter.isupper() for letter in list(word)]
    # Indexes of upper-cased letters
    upper_cased_indexes = [index for index, is_upper in enumerate(is_uppercase) if is_upper]

    # Lowercase the word
    word = word.replace('I', 'ı').replace('İ', 'i').lower()

    sait_list = ['a', 'ı', 'o', 'u', 'e', 'ə', 'i', 'ö', 'ü']  # All "sait"s in Azerbaijani language
    # Mənsubiyyət, yiyə lik, yönlük, təsirlik suffixes set

    if type(wordlist) == list: wordlist = set(wordlist)  # To ensure the wordlist is in a set format

    # If the word is in its stemmed format or in the exception list return it
    if word in {*wordlist, *exception_list, *auxiliary}:
        return uppercase(word, upper_cased_indexes)  # Reinstate previously upper-cased letters if there is
    
    index_daki = word.find('dakı')
    index_deki = word.find('dəki')

    if index_daki != -1:

        return uppercase(word[:index_daki + 4], upper_cased_indexes)
        
    elif index_deki != -1:

        return uppercase(word[:index_deki + 4], upper_cased_indexes)
        
    lar_ler_bool = lar_ler(word, wordlist)

    # If there is no "lar" "lər" in the word(or there is but the part that comes before the "lar" "lər" is not
    # in wordlist) and length of given word is greater than 1, then add "maq" "mək" and check that part in a wordlist
    if not lar_ler_bool and len(word) > 1:
        maq_mek_output = maq_mek(word, upper_cased_indexes, wordlist)
        if maq_mek_output != '-1':
            return maq_mek_output

    for index in range(1, len(word)):
        # if there is hyphen at the end of word[:-index] stop searching otherwise it will remove it
        # adamlar-ın != adam || adamların = adam
        if word[:-index][-1] == '-':
            break

        # et-edir and get- gedir rule
        if word[:-index] in ['ed', 'ged'] and word[-index] in sait_list:
            word = word[:-index][:-1] + 't' + word[-index:]

        # Checking the q-ğ rule
        if word[:-index] not in wordlist and word[:-index][-1] == "ğ" and word[-index] in sait_list:
            # If adjusted form's stem is in the list change the word
            if ğ_to_q(word, index)[:-index] in wordlist:
                word = ğ_to_q(word, index)

        # Checking the k-y rule
        if word[:-index] not in wordlist and word[:-index][-1] == "y" and word[-index] in sait_list:
            # If adjusted form's stem is in the list change the word(yedi!= kedi)
            if y_to_k(word, index)[:-index] in wordlist:
                word = y_to_k(word, index)

        # Checking exception nouns rule
        if word[:-index] not in wordlist and word[:-index] in exception_nouns:
            # Checking any intersection. Since max length of 'mensubiyyet_hal''s element is 4 range is [1, 5)
            if bool(set([word[-index:][:i] for i in range(1, 5)]) & mensubiyyet_hal):
                word = reinstate_vowel(word, exception_nouns, index)

        # If word[:-index] is in the wordlist return it as a stem of given word
        if word[:-index] in wordlist:
            word = uppercase(word, upper_cased_indexes)  # Reinstate previously upper-cased letters if there is
            return word[:-index]

        # The same rule that is written above("lar" "lər" and length has to be greater than 1)
        if not lar_ler_bool and len(word[:-index]) > 1:
            maq_mek_output = maq_mek(word[:-index], upper_cased_indexes, wordlist)
            if maq_mek_output != '-1':
                return maq_mek_output
            else:
                if word[:-index][-1] == "d" and word[-index] in sait_list and len([l for l in list(word[:-index]) if l in sait_list]) > 1:
                    maq_mek_output = maq_mek(word[:-index][:-1] + 't', upper_cased_indexes, wordlist)
                    if maq_mek_output != '-1':
                        return maq_mek_output
    

    # If can not find the stem return the word itself
    return uppercase(word, upper_cased_indexes)  # Reinstate previously upper-cased letters if there is




def surname_stem(word: str, model, w2i, idx2tag) -> str:

    """
    Splits a surname into two parts: the first part includes the surname up to and including the last dot,
    and the second part includes the remainder of the surname after and excluding the last dot. If the surname contains
    uppercase characters separated by dots, it stems the second part and returns the joined stemmed word.

    Args:
        word (str): The surname to be split and stemmed.

    Returns:
        str: The final stemmed surname, where the second part is stemmed if 'word' contains uppercase characters
        separated by dots.
    """

    dot_between_uppercase = re.search(r'((?:[A-ZƏİŞĞÖÜIÇ]\.)+)([A-ZƏİŞĞÖÜIÇ])', word)
    
    if dot_between_uppercase:
        last_dot_index = dot_between_uppercase.end(1) - 1
        first_part = word[:last_dot_index + 1] 
        second_part = word[last_dot_index + 1:]

        stemmed_second_part = stem_sentence(second_part, model, w2i, idx2tag, return_list = False)
        
        joined_word = first_part + stemmed_second_part

        return joined_word
    
    return word