import string

def sentenceNormalizer(sentence):
    punctuationCuller = str.maketrans("", "", string.punctuation)
    sentenceNormalized = sentence.translate(punctuationCuller).lower()

    noWhitespaceSentence = ""
    for character in sentenceNormalized:
        if not character.isspace():
            noWhitespaceSentence += character

    sentenceNormalized = noWhitespaceSentence

    return sentenceNormalized

sentenceList = []
file = open("sample-file.txt", "r")
for line in file:
    sentenceList.append(line.rstrip("\n"))
file.close()

normalizedSentenceGroups = {}

for lineNumber, line in enumerate(sentenceList, start=1):
    if line.strip() == "":
        continue

    normalizedSentence = sentenceNormalizer(line)

    if normalizedSentence not in normalizedSentenceGroups:
        normalizedSentenceGroups[normalizedSentence] = []

    normalizedSentenceGroups[normalizedSentence].append((lineNumber, line))

nearDuplicateSets = []

for group in normalizedSentenceGroups.values():
    if len(group) >= 2:
        nearDuplicateSets.append(group)

print(len(nearDuplicateSets))

for index, sentenceGrouping in enumerate(nearDuplicateSets[:2], start=1):
    print(f"\nSet {index}:")
    for lineNumber, text in sentenceGrouping:
        print(f"{lineNumber}: {text}")