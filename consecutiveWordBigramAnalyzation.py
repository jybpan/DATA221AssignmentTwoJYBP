import string

file = open("sample-file.txt", "r")

tokenList = []
bigramList = []

punctuationCuller = str.maketrans('', '', string.punctuation)

with file:
    for line in file:
        for word in line.split():
            cleanWord = word.lower()
            cleanWord = word.translate(punctuationCuller)

            if len(cleanWord) >= 2:
                tokenList.append(cleanWord)

tokenListLength = range(len(tokenList))
print(tokenListLength)

for indexOne in tokenListLength:
    for indexTwo in tokenListLength:
        if indexOne <= tokenListLength-1:
            print(indexOne, indexTwo)
            bigramList.append(tokenList[indexOne], " ", tokenList[indexTwo])

print(bigramList)