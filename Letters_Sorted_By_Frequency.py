# from Five_Letter_Words import word_list_5_letters

# To be replaced with list of all 5 letter words from Five_Letter_Words
word_list_5_letters = 'clash, sunks, nicer, musts, tatty, emote, build, bolds, guard, aimed, derby, filed, fakes, novel, close, doffs, leapt, acted, sloes, bores, biddy, shins, amiss, ducts, hoard, purse, endow, codas, abort, poets'.split(',')
word_list_5_letters = [word.upper().strip() for word in word_list_5_letters]
print(word_list_5_letters, '\n')

# Count how many occurrences there are of each letter across all of the 5 letter words.
letter_frequency_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0,
                         'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
for word in word_list_5_letters:
    for letter in word:
        letter_frequency_dict[letter] += 1
#print(letter_frequency_dict)
print(letter_frequency_dict, '\n')

# Create list of tuples of the form (letter, frequency), and sort by decreasing frequency.
letter_frequencies = list(letter_frequency_dict.items())
letter_frequencies = sorted(letter_frequencies, key=lambda x: x[1])[::-1]
print(letter_frequencies, '\n')

# Create list of just letters, sorted by decreasing frequency.
letters_sorted_by_frequency = [pair[0] for pair in letter_frequencies]
print(letters_sorted_by_frequency)

