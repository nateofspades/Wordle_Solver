import pandas as pd
import nltk
nltk.download('words')
from nltk.corpus import words

# Extract all words in the dictionary
word_list = words.words()
print(len(word_list))

# Extract the 5-letter words. Make them uppercase.
word_list_5_letters = []
for word in word_list:
    if len(word) == 5:
        word = word.upper()
        word_list_5_letters.append(word)

# Remove duplicates
word_list_5_letters = list(set(word_list_5_letters))

# Outputs 9972, i.e. there are 9972 5-letter words to be annotated.
print(len(word_list_5_letters))

df = pd.DataFrame(word_list_5_letters)
print(df.head(50))
