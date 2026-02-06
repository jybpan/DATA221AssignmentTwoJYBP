import string
import pandas as pd

file = open("sample-file.txt", "r")

tokenList = []
tokenDictionary = {}

# Makes a translation table, deletes any string containing the basic ascii punctuation characters
# ' ' is simply to make sure that nothing else is deleted from the stirng, only punctuation
punctuationCuller = str.maketrans('', '', string.punctuation)

with file:
    for line in file: 
        for word in line.split():
            cleanWord = word.lower()
            cleanWord = cleanWord.translate(punctuationCuller)

            if len(cleanWord) >= 2:
                tokenList.append(cleanWord)

tokenListAndFrequency = pd.Series(tokenList).value_counts().head(10)

for word, frequency in tokenListAndFrequency.items():
    print(f"{word} -> {frequency}",end=" ")