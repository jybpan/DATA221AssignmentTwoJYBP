import string

file = open("sample-file.txt", "r")

tokenList = []
uniqueTokenList = []
tokenDictionary = {}
keySortedTokenDictionary = {}

punctuationCuller = str.maketrans('', '', string.punctuation)

with file:
    for line in file: 
        for word in line.split(): # "Python is so readable bro!" The 4 indents in question:
            cleanWord = word.lower()
            cleanWord = cleanWord.translate(punctuationCuller)

            if len(cleanWord) >= 2:
                tokenList.append(cleanWord)

tokenDictionary = {words: tokenList.count(words) for words in set(tokenList)}

for key in sorted(tokenDictionary, key=tokenDictionary.get):
    keySortedTokenDictionary[key] = tokenDictionary[key]

print(keySortedTokenDictionary)