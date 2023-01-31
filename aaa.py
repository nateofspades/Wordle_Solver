# from Five_Letter_Words import word_list_5_letters

# To be replaced with list of all 5 letter words from Five_Letter_Words
word_list_5_letters = 'clash, sunks, nicer, musts, tatty, emote, build, bolds, guard, aimed, derby, filed, fakes, novel, close, doffs, leapt, acted, sloes, bores, biddy, shins, amiss, ducts, hoard, purse, endow, codas, abort, poets'.split(',')
word_list_5_letters = [word.upper().strip() for word in word_list_5_letters]
print(word_list_5_letters, '\n')

def subword_score(subword):
    """
    subword is a list of length 5. If the i'th letter is known, then it is filled in in the list. Otherwise it is '_'.
    e.g. if the first letter is 'A', the third letter is 'D', but the others are unknown, then subword is ['A', '_', 'D', '_', '_'].
    """


def candidate_words(word_list, correct_word):

    first_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    second_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    third_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    fourth_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    fifth_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for word in word_list:



def word_predictor(candidate_word_list, correct_word):
