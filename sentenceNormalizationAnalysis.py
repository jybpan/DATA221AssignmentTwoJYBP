import string
import pandas as pd

file = open("sample-file.txt", "r")

sentenceList = []
sentenceNormalizedList = {}
sentenceDictionaryMapping = {} #Maps sentences to their normalized sentence form

punctuationCuller = str.maketrans(' ', ' ', string.punctuation)

def sentenceNormalizer(sentence, punctuationCuller):
    sentenceNormalized = sentence.translate(punctuationCuller)
    sentenceNormalized = sentence.lower()
    sentenceNormalized = sentence.replace('\n', '')
    sentenceNormalized = sentence.replace(' ', '')
    print(f"EDITED LINE: {sentenceNormalized}")
    return sentenceNormalized


with file:
    for line in file:
        print("NEW LINE: ", line)
        normalizedSentence = sentenceNormalizer(line, punctuationCuller)
        sentenceDictionaryMapping[line] = normalizedSentence

print(sentenceDictionaryMapping.values())