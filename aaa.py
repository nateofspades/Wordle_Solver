# from Five_Letter_Words import word_list_5_letters

# To be replaced with list of all 5 letter words from Five_Letter_Words
word_list_5_letters = 'clash, sunks, nicer, musts, tatty, emote, build, bolds, guard, aimed, derby, filed, fakes, novel, close, doffs, leapt, acted, sloes, bores, biddy, shins, amiss, ducts, hoard, purse, endow, codas, abort, poets'.split(',')
word_list_5_letters = [word.upper().strip() for word in word_list_5_letters]
print(word_list_5_letters, '\n')


def wordle_display(predicted_word, correct_word):

    display = ['grey', 'grey', 'grey', 'grey', 'grey']

    # Fill in green Wordle letters.
    for i in range(5):
        if predicted_word[i] == correct_word[i]:
            display[i] = 'green'

    # Identify indices of non-green letters.
    non_green_indices = []
    for index in range(5):
        if display[index] == '_'
            non_green_indices.append(index)

    # Fill in yellow Wordle letters
    for index in non_green_indices:



    return display

print(wordle_display('shape', 'sheep'))



# def word_list_subsetter():
#     """
#     Based on wordle_display
#     """

#
# def next_prediction(word_list, correct_word, L1='', L2='', L3='', L4='', L5=''):
#     """
#     """
#     word = word_list[0]
#     if word = correct_word:
#         print(word)
#     else:
#         correct_L1 = correct_word[0]
#         correct_L2 = correct_word[1]
#         correct_L3 = correct_word[2]
#         correct_L4 = correct_word[3]
#         correct_L5 = correct_word[4]
#
#
#
#
#
#
# def predict_word(L1='', L2='', L3='', L4='', L5=''):
#     prediction = '_____'
#     candidate_words = word_list_5_letters
#     while (len(candidate_words) > 0) and  ('_' in prediction):
#         candi
#
#
#
#     if L1 != '':
#
#
# def subword_score(subword):
#     """
#     subword is a list of length 5. If the i'th letter is known, then it is filled in in the list. Otherwise it is '_'.
#     e.g. if the first letter is 'A', the third letter is 'D', but the others are unknown, then subword is ['A', '_', 'D', '_', '_'].
#     """
#
#
# # def candidate_words(word_list, correct_word):
# #
# #     first_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #     second_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #     third_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #     fourth_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #     fifth_letter_candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# #
# #     for word in word_list:
#
#
#
# def word_predictor(candidate_word_list, correct_word):
