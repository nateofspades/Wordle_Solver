import numpy as np

predicted_word = 'peels'
colors = ['green', 'yellow', 'grey', 'green', 'grey']
# correct_word = 'p__l_'

# Identify which indices in predicted_word correspond to green letters.
green_indices = []
for i in range(5):
    if colors[i] == 'green':
        green_indices.append(i)

# Subset the word_list to only include words which match the green letters at the same indices.
# for index in green_indices:
#     green_letter = predicted_word[index]
#     word_list = [word for word in word_list if word[index] == green_letter]

# Identify which indices in predicted_word correspond to grey or yellow letters.
blank_indices = []
for i in range(5):
    if colors[i] != 'green':
        blank_indices.append(i)

# Subset the word_list to exclude words which match any of the yellow or grey letters at the same index.
# for index in blank_indices:
#     for word in word_list:
#         if word[index] == predicted_word[index]:
#             word_list.remove(word)

# For the non-green predicted letters, counting how many yellows and how many greys there are for each.
dict = {}
for index_1 in blank_indices:
    letter_1 = predicted_word[index_1]
    if letter_1 not in dict:
        dict[letter_1] = {'grey_count':0, 'yellow_count':0}
        for index_2 in blank_indices:
            letter_2 = predicted_word[index_2]
            if letter_1 == letter_2:
                if colors[index_2] == 'grey':
                    dict[letter_1]['grey_count'] += 1
                if colors[index_2] == 'yellow':
                    dict[letter_1]['yellow_count'] += 1

import pprint
pprint.pprint(dict)

# For each non-green predicted letter, if grey_count >=1 then the number of occurrences of that letter in the blanks is yellow_count.
# For each non-green predicted letter, if grey_count = 0 then the number of occurrences of that letter is >= yellow_count.
# Remove all words from word_list which do not satisfy the appropriate property.
for word in word_list:
    letters_at_blank_locations = np.array([word[i] for i in blank_indices])
    for letter in dict:
        if (dict[letter]['grey_count'] >= 1) and (letters_at_blank_locations[letters_at_blank_locations==letter].sum() != dict[letter]['yellow_count']):
            word_list.remove(word)
        if (dict[letter]['grey_count'] == 0) and (letters_at_blank_locations[letters_at_blank_locations==letter].sum() < dict[letter]['yellow_count']):
            word_list.remove(word)



