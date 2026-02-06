import string
import pandas as pd

file = open("sample-file.txt", "r")

tokenList = []
bigramList = []
bigramsAndFrequency = {}

punctuationCuller = str.maketrans('', '', string.punctuation)

with file:
    for line in file:
        for word in line.split():
            cleanWord = word.lower()
            cleanWord = word.translate(punctuationCuller)

            if len(cleanWord) >= 2:
                tokenList.append(cleanWord)

tokenListLength = len(tokenList)
tokenListRange = range(tokenListLength)

for index in tokenListRange:
    nextIndex = index+1
    if nextIndex <= len(tokenList)-1:
        bigramList.append((f"{tokenList[index]} {tokenList[nextIndex]}"))

bigramsAndFrequency = pd.Series(bigramList).value_counts().head(5)

for word, frequency in bigramsAndFrequency.items():
    print(f"{word} -> {frequency}", end=" ")