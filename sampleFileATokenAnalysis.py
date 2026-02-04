import string

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

# Finds the counts/frequency of each word, counts how many times a certain string
# appears within tokenList. Uses a set to count each word once, as sets only allow unique strings/tokens.
tokenDictionary = {words: tokenList.count(words) for words in set(tokenList)}

# Creates a sorted by descending order tuple, and then slicing it so it only has the first 10 elements.
mostFrequentTokens = sorted(tokenDictionary.items(), key=lambda keyValuePair: keyValuePair[1], reverse=True)[:10]

for key, value in mostFrequentTokens:
    print(key, "->", value, end=", ")
