import re  # Regex library
import json  # For reading json file
# POS-Tagging related imports
import torch
from config import UNIQUE_TAGS
from pos_utils import predict_sentence, load_pickle
from preprocessing import sent_without_punctuation
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


def uppercase(word: str, indexes: list) -> str:
    """
    word - lowercase, stemmed version
    indexes - list of uppercase letters to change
    expected value to return -> str

    This function reinstates the upper-cased letters in the original format of the word. The 'stemmer()' function
    lowercases the input word in order to search it in the 'wordlist', since all words in the 'wordlist' are in lower-
    cased format.
    Args:
        word: The lower-cased and stemmed format of the original word.
        indexes: The indexes of the upper-cased letters in the original word.

    Returns:
        The reinstated format of lower-cased word.
    """
    return "".join(
        [letter.replace('i', 'İ').upper() if index in indexes else letter for index, letter in enumerate(list(word))])

"""
    Enumerate creates pairs of letters and their indexes
    Then we check if there's an index that's in the indexes list
    If yes, we make it uppercase, + special case for 'i'
    
    Enumerate(list(word)) converts the input string word into a list of its characters 
    Associates each character with its index (position) in the original string
    This creates pairs of (index, letter) for each character in word

    The result is a list of characters, where some may be transformed 
    (due to 'i' replacement and uppercase conversion) and others may remain the same.
"""


def load_allwords() -> set:
    """
    This function loads all words in a stemmed format.
    """
    # Open a file that contains all words in Azerbaijani language
    file = open(r'ML_Utils/data/all_words_pure.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file.readlines()}


"""
    Reads file with all Azerbaijani words
    Since they are line by line, it gets rids of \n
    Returns a set of lowercased words, ('i' special case) from txt file
    Hello
    World       -> {'hello', 'world'}

"""

def load_locations() -> set:
    """
    This function loads all geographical locations in Azerbaijani language.
    """
    # Open a file that contains all names of geographical locations in Azerbaijani language
    file = open(r'ML_Utils/data/cografi_adlar.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file.readlines()}


def load_verb() -> set:
    """
    This function loads all geographical locations in Azerbaijani language.
    """
    # Open a file that contains all names of geographical locations in Azerbaijani language
    file = open(r'ML_Utils/data/verb.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file.readlines()}


def load_pronoun() -> set:
    """
    This function loads all geographical locations in Azerbaijani language.
    """
    # Open a file that contains all names of geographical locations in Azerbaijani language
    file = open(r'ML_Utils/data/pronoun.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file.readlines()}



def load_pronoun() -> set:
    """
    This function loads all geographical locations in Azerbaijani language.
    """
    # Open a file that contains all names of geographical locations in Azerbaijani language
    file = open(r'ML_Utils/data/pronoun.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file.readlines()}



def load_names() -> set:
    """
    This function loads all names in Azerbaijani language.
    """
    # Open a file that contains all names in Azerbaijani language
    file_names = open(r'ML_Utils/data/az_names.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file_names.readlines()}

"""
    Reads file with all Azerbaijani names
    Since they are line by line, it gets rids of \n
    Returns a set of lowercased words, ('i' special case) from txt file
    Hello
    World       -> {'hello', 'world'}
"""

def load_surnames() -> set:
    """
    This function loads all names in Azerbaijani language.
    """
    # Open a file that contains all names in Azerbaijani language
    file_names = open(r'ML_Utils/data/all_surnames.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "").replace('I', 'ı').replace('İ', 'i').lower() for word in file_names.readlines()}


"""
    Reads file with all Azerbaijani names
    Since they are line by line, it gets rids of \n
    Returns a set of lowercased words, ('i' special case) from txt file
    Hello
    World       -> {'hello', 'world'}
"""


def load_auxiliary() -> set:
    """
    This function loads auxiliary part of speech tags that are not omonim with other part of speech tags
    """
    # Open a file that contains these auxiliary part of speech tags
    file_auxiliary = open(r'ML_Utils/data/auxiliary.txt', 'r', encoding='utf-8')

    # Delete all '\n' that appear at the end of the words and lowercase them then return
    return {word.replace('\n', "") for word in file_auxiliary.readlines()}

"""
    Reads file with all Azerbaijani auxiliary words
    Since they are line by line, it gets rids of \n
    Returns a set of words, ('i' special case) from txt file
    Hello
    World       -> {'hello', 'world'}
    They are all lowercased from the beginning, no need to lowercase
"""


def load_exceptions() -> dict:
    """
    This function loads the exception nouns list that lose their vowel while adding "mənsubiyyət", "təsirlik", "yönlük",
    "yiyəlik" suffixes.
    """
    # File of exception nouns list that lose their vowel while adding mənsubiyyət, təsirlik, yönlük, yiyəlik suffixes
    file_exception_nouns = open(r'ML_Utils/data/isim_mənsubiyyət_hal_sait_düşən.json', 'r', encoding='utf-8')
    exception_nouns = json.load(file_exception_nouns)  # Loading json file as a dictionary
    return exception_nouns

"""
    Load json file that contains all exceptions like "ağl: ağıl"
    Turn it into dictionary
"""



def remove_punctuations(word: str) -> str:
    """
    Removes all punctuations except hyphen(-), retains commas or dots between numbers,
    keeps dots between two capital letters, and keeps colons between numbers.

    Args:
        word (str): The word that will be processed.

    Returns:
        str: The processed format of the word.

    a-z: Matches lowercase English letters from 'a' to 'z'.
    A-Z: Matches uppercase English letters from 'A' to 'Z'.
    Ə: Matches the character 'Ə'. same for all letters there
    ə: Matches the character 'ə'. same for all letters there
     \d: Matches any digit (0-9).
    -: Matches a hyphen character.
    +: Specifies that the characters mentioned should be matched one or more times.
    """
    email_pattern = re.compile(r'\S+@\S+')
    file_name_pattern = re.compile(r'([^\s]+\.(?:csv|txt|html|xml|jpg|class|java|cvs|doc|docx|exe|gif|htm|html|jpg|jpeg|pdf|png|ppt|pptx|tar|wav|xls|xlsx|zip))')
    url_pattern = re.compile(r"((?:w{3}\.)?[a-zA-Z0-9ƏİŞĞÖÜIÇəi̇şğöüçı]+?\.(?:com|net|org|edu|gov|kg|asia|cat|info|int|jobs|mobi|museum|name|post|pro|tel|travel|ai|az|biz|et|eu|fr|ne|ru|sh|tr|tv|ua|uk|us|ws))")

    if email_pattern.match(word) or file_name_pattern.match(word) or url_pattern.match(word):
        return word
    else: 
        first_version = "".join(re.findall(r"[\w%-]+|-|(?<=[A-ZƏİŞĞÖÜIÇ])\.(?=[A-ZƏİŞĞÖÜIÇ])|(?<=\d)[,.](?=\d)|(?<=\d):(?=\d)", word))
        return "".join(re.split(r"(?:(?<![a-zA-ZƏİŞĞÖÜIÇəi̇şğöüçı\d])-|-(?![a-zA-ZƏİŞĞÖÜIÇəi̇şğöüçı\d])|\.$|(?<=\w)(?=[^a-zA-ZƏİŞĞÖÜIÇəi̇şğöüçı\d]))", first_version))


def maq_mek(word: str, upper_cased_indexes: list, wordlist: set) -> str:
    """

    Args:
        word:
        upper_cased_indexes:

    Returns:

    """
    if word != "" and word + "maq" in wordlist:
        return uppercase(word, upper_cased_indexes) + "maq"
    

    if word != "" and word + "mək" in wordlist:
        return uppercase(word, upper_cased_indexes) + "mək"
    return '-1'


def lar_ler(word: str, wordlist: set) -> bool:
    """
    This function returns "True" if the part that comes before "lar" or "lər" is in the wordlist. Returns "False"
    otherwise. The purpose of these function is to prevent adding the "maq" "məq" suffixes to these kind of words.

    
    *When you want to add a suffix like "maq" or "mək" to a word
    you can first call the lar_ler function with the word as an argument.

    If lar_ler returns True, it means the input word is already in its plural form
    and you can choose not to add the "maq" or "mək" suffix because it's not necessary for plural words.

    If lar_ler returns False, it means the input word is not in its plural form
    and you can proceed to add the "maq" or "mək" suffix as needed.


    Args:
        word: The given word.
        wordlist: The words list that will be used for finding the part that comes before "lar" or "lər".

    Returns:
        Whether the part before the "lar" or "lər" in the wordlist or not.

    """
    if word.find("lar") != -1 and word[:word.find("lar")] in wordlist:
        return True
    if word.find("lər") != -1 and word[:word.find("lər")] in wordlist:
        return True
    return False


"""
    Checks if a given word is in its plural form  by looking for "lar" or "lər"
    Then checks if the part before these suffixes exists in the provided wordlist

    word.find("lər"): finds the index of the first occurrence of the substring "lər" within the string word. 
    It returns the index where "lər" starts within the string. If "lər" is not found in word, it returns -1.

    word[:word.find("lər")]: takes the result from step 1, which is the index where "lər" starts
    and uses it to create a slice of the string word. 

    The slice notation [:index] indicates that you want to extract the part of the string 
    from the beginning (index 0) up to, but not including, the index you specified.

    By doing this, finds lar-ler, deletes it, looks for the word without lar-ler in the wordlist
    if it finds it in the wordlist, return True
    otherwise return False



    If the word does not contain "lar" or "lər," the function returns False immediately.
    If the word contains "lar" or "lər," it checks if the part of the word before the first occurrence of "lar" or "lər" is present in the provided wordlist.
    If it is present, the function returns True, indicating that the word is in its plural form.
    If it is not present, the function returns False, indicating that the word is not in its plural form.

"""


def pos_tag_predict(text, model, w2i, idx2tag):

    sentence_tokens, tokens_with_index = sent_without_punctuation(text, ready_for_model=True)
    score, tags = predict_sentence(model, sentence_tokens, w2i, idx2tag)
    ent_label_list = []

    for indexes, tag in zip(tokens_with_index, tags):
        word = text[indexes[1][0]:indexes[1][1]]
        ent_label_list.append({"label": tag, "word": word})

    doccano_output = []
    temp_d = {}
    for dict_label in ent_label_list:
        label_base = dict_label['label'].split('/')[0]
        
        if label_base not in ['B', 'M', 'E']:
            doccano_output.append({"label": dict_label['label'].split('/')[-1], "word": dict_label['word']})
        else:
            if label_base == 'B':
                temp_d['label'] = dict_label['label'].split('/')[1]
                temp_d['word'] = dict_label['word']
            elif label_base == 'M' and 'word' in temp_d:
                # Append the current word to the existing word in temp_d
                temp_d['word'] += ' ' + dict_label['word']
            elif label_base == 'E':
                # Ensure there's an ongoing entity to end
                if 'word' in temp_d:
                    temp_d['word'] += ' ' + dict_label['word']
                    doccano_output.append(temp_d)
                    temp_d = {}
                else:
                    # Handle case where 'E' appears without a preceding 'B'
                    doccano_output.append({"label": dict_label['label'].split('/')[-1], "word": dict_label['word']})
            else:
                # Handle isolated 'B' or 'E' labels by resetting temp_d
                temp_d = {}

    doccano_temp = []
    for dict_label in doccano_output:
        if dict_label['label'] == "Feil-İnkar/Feil-Sifət":
            doccano_temp.append({"label": "Feil-Sifət", "start_offset": dict_label['start_offset'],
                                 "end_offset": dict_label['end_offset']})
            doccano_temp.append({"label": "Feil-İnkar", "start_offset": dict_label['start_offset'],
                                 "end_offset": dict_label['end_offset']})

        else:
            doccano_temp.append(dict_label)
        
    doccano_output = doccano_temp
    doccano_temp = []
    for dict_list in doccano_output:
        if '/' in dict_list['label']:

            if text[dict_list["start_offset"]:dict_list["end_offset"]][-3:] in ['dək', 'tək', 'can', 'cən']:

                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[0], "start_offset": dict_list['start_offset'],
                     "end_offset": dict_list['end_offset'] - 3})
                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[1], "start_offset": dict_list['end_offset'] - 3,
                     "end_offset": dict_list['end_offset']})

            elif text[dict_list["start_offset"]:dict_list["end_offset"]][-4:] in ['sana']:

                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[0], "start_offset": dict_list['start_offset'],
                     "end_offset": dict_list['end_offset'] - 4})
                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[1], "start_offset": dict_list['end_offset'] - 4,
                     "end_offset": dict_list['end_offset']})


            else:
                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[0], "start_offset": dict_list['start_offset'],
                     "end_offset": dict_list['end_offset'] - 2})
                doccano_temp.append(
                    {"label": dict_list['label'].split('/')[1], "start_offset": dict_list['end_offset'] - 2,
                     "end_offset": dict_list['end_offset']})
        else:
            doccano_temp.append(dict_list)
       
    doccano_output = doccano_temp
    final_output = []
    for item in doccano_output:
        words = item['word'].split()  # Split the 'word' string into a list of words
        if len(words) > 1:
            # Process all but the last word with the label "İsim"
            for word in words[:-1]:
                final_output.append({'label': 'İsim', 'word': word})
            # Add the last word with the original label
            final_output.append({'label': item['label'], 'word': words[-1]})
        else:
            final_output.append(item)

    return final_output


import os
import torch

def load_pos_model():
    """
    The function that loads the POS tagger model.
    Returns:
        It returns the model and other necessary things for prediction
    """
    model_path = os.path.join(os.path.dirname(__file__), 'stem_models\model.pth')
    tag2idx = {tag: idx for idx, tag in enumerate(UNIQUE_TAGS)}
    idx2tag = {idx: tag for tag, idx in tag2idx.items()}

    device = "cpu"
    model_path = r"C:\Users\Nifdi Guliyev\Documents\GitHub\aznlp\model.pth"
    model = torch.load(
        model_path,
        map_location=lambda storage, loc: storage)
    model = model["model"]
    model.eval()
    model.crf.device = device
    model.device = device

    w2i_path = os.path.join(os.path.dirname(__file__), 'stem_models\word2index.pkl')
    w2i = load_pickle(w2i_path)

    return model, w2i, idx2tag
