def tokenizer(string):
    str_SEN = ""
    str_ = ""
    string = string.strip()
    string += ' '
    for char in string:
        if char.isnumeric() or char.isalpha():

            str_ += char

        else:
            if str_ != "":
                str_SEN += str_ + " "
                str_ = ""
            if char != " ":
                str_SEN += char + " "

    return str_SEN.strip()


def sent_without_punctuation(given_sent: str, ready_for_model=False, inside_punc=False) -> list:
    """
    This function tokenizes sentence into words without taking the punctuations that are in the beginning or ending
    of the word.

    Args:
        given_sent: Given sentence to process.
        ready_for_model: If 'True' the function returns a list that consists of tokens that are extracted.
    Return:
        tokenized_sent: Tokenized sentence without punctuation.
        :param given_sent:
        :param ready_for_model:
        :param inside_punc:
        :return:

    """
    tokens_and_indexes = []  # The list that will store tokens and their indexes in the given sentence.
    list_tokens = []  # List of extracted tokens for the model.
    # token_with_inside = [] # Will probably removed.
    token = ""  # The initial version of token.
    index = 0  # Initial index for token.

    for char in given_sent:

        acceptable_char = False
        if not char.isalnum() and index not in {0, len(given_sent) - 1}:
            # If the punctuation is in the middle accept this char as a part of token.
            if given_sent[index - 1].isalnum() and given_sent[index + 1].isalnum():
                acceptable_char = True

        if char == " " and token != "":
            tokens_and_indexes.append((given_sent[begin:end + 1], [begin, end + 1]))
            list_tokens.append(given_sent[begin:end + 1])
            # token_with_inside.append((token, [begin, end + 1]))
            token = ""
        else:
            if char.isalnum() or acceptable_char:
                if token == "":
                    begin = index
                token += char
                end = index
        index += 1
    if token != "":
        tokens_and_indexes.append((given_sent[begin:end + 1], [begin, end + 1]))
        list_tokens.append(given_sent[begin:end + 1])
        # token_with_inside.append((token, [begin, end + 1]))
    if ready_for_model:
        return list_tokens, tokens_and_indexes
    # if inside_punc:
    # return token_with_inside
    return tokens_and_indexes


def index_matcher(org_str: str, tknd_str: str) -> list:
    """
    This function returns tknd_str's token's indexes in original string.

    Args:
        org_str(str): Original string. The raw string, means before tokenized.
        tknd_str(str): Tokenized format of original string(org_str).

    Returns:
        indexes_org(list): Corresponding indexes of tokens in original string(org_str)

    """
    indexes_org = []
    boundary = 0
    for word in tknd_str.split():
        start = org_str[boundary:].find(word)
        end = start + len(word)
        indexes_org.append((start + boundary, end + boundary))
        boundary = end

    return indexes_org