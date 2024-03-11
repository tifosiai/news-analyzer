def ğ_to_q(word: str, index: int) -> str:
    """
    The 'stemmer()' function first searches word[:-i] (for instance 'uşağ') in a wordlist. If does not find,
    it checks last letter of the word[:-i]. If it is 'ğ' and the letter that comes after the 'ğ' is vowel, it sends
    the word to 'ğ_to_q()' function in order to apply the following rule:
        If the word ends with the letter 'q', while adding suffix that starts with vowel due to
        Azerbaijani grammatical rule 'q' becomes 'ğ' (e.g., 'uşaq' -> 'uşağın', 'ocaq' -> 'ocağın').

    Args:
        word: The word that has to be changed.
        index: The index that helps to find the part of the word where the rule has to be applied.

    Returns:
        The changed format of the given word.
    """
    return word[:-index][:-1] + 'q' + word[-index:]


def y_to_k(word: str, index: int) -> str:
    """
    The 'stemmer()' function first searches word[:-i] (for instance 'biliy') in a wordlist. If does not find,
    it checks last letter of the word[:-i]. If it is 'y' and the letter that comes after the 'y' is vowel, it sends
    the word to 'y_to_k()' function in order to apply the following rule:
        If the word ends with the letter 'k', while adding suffix that starts with vowel due to
        Azerbaijani grammatical rule 'k' becomes 'y' (e.g., 'bilik' -> 'biliyin', 'nazirlik' -> 'nazirliyin').

    Args:
        word: The word that has to be changed.
        index: The index that helps to find the part of the word where the rule has to be applied.

    Returns:
        The changed format of the given word.
    """
    return word[:-index][:-1] + 'k' + word[-index:]


def reinstate_vowel(word: str, exception_nouns: dict, index: int) -> str:
    """
    Some nouns in the Azerbaijani language lose their vowel in the last syllable while adding mənsubiyyət, təsirlik,
    yönlük, yiyəlik suffixes. For instance, the noun 'abır' becomes 'abr'('abır' + 'ın' --> 'abrın'). The 'stemmer()'
    function first searches 'abr'(as word[:-i]) in the wordlist. If does not find, it searches  'abr'(as word[:-i])
    in 'exception_nouns'. If finds it then searches suffix(as word[-index:][:i]) in 'mensubiyyet_hal' set.

    After verifying that the suffix that is added to the stem is in 'mensubiyyet_hal' set the 'reinstate_vowel()'
    function reinstates the vowel (e.g. 'abrın' --> 'abırın').

    Args:
        word: The word that has to be changed.
        exception_nouns: Exception nouns that lose their vowel while adding special suffixes in a dictionary format.
        'value's of this dictionary are the original nouns, and 'key's of the dictionary are the version of the nouns
        when they lose their vowel.
        index: The index that indicates position of the probable stem.

    Returns:
        The modified version of the word
    """
    return exception_nouns[word[:-index]] + word[-index:]
