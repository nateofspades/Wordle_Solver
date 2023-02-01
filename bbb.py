import numpy as np

predicted_word = ['p','e','e','l','s']
display = ['green', 'yellow', 'grey', 'green', 'grey']

correct_word = ['p', '_', '_', 'l', '_']

yellow_or_grey_indices = []
for i in range(5):
    if display[i] != 'green':
        yellow_or_grey_indices.append(i)
yellow_or_grey_letters = [predicted_word[index] for index in yellow_or_grey_indices]
print(yellow_or_grey_letters)

dict = {}
for i in range(5):
    if display[i] != 'green':
        letter_i = predicted_word[i]
        if letter_i not in dict:
            dict[letter_i] = {'yellow_count':0, 'grey_count':0}
            for j in range(5):
                letter_j = predicted_word[j]
                if letter_j == letter_i:
                    if display[j] == 'yellow':
                        dict[letter_i]['yellow_count'] += 1
                    if display[j] == 'grey':
                        dict[letter_i]['grey_count'] += 1

import pprint
pprint.pprint(dict)


