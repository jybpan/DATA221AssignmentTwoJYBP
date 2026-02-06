import string
import pandas as pd

file = open("sample-file.txt", "r")

sentenceList = []
sentenceNormalizedList = {}

punctuationCuller = str.maketrans(' ', ' ', string.punctuation)

with file:
    for line in file:
       sentenceList.append(line)

for element in sentenceList:
    sentenceNormalizedList = element.replace('\n', '')
    sentenceNormalizedList = elemenet.lower()
    

print(sentenceNormalizedList)