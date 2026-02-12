def findLinesContaining(fileName, keyword):    
    matches = []
    file = open(fileName, "r")
    lineNumber = 1
    lowerKeyword = keyword.lower()
    
    for line in file:
        if lowerKeyword in line.lower():
            matches.append((lineNumber, line.rstrip()))
        lineNumber += 1
    
    file.close()
    
    return matches

results = findLinesContaining("sample-file.txt", "lorem")

print(f"Number of matching lines: {len(results)}")
print(f"\nFirst 3 matching lines:")

for entry in results[:3]:
    print(entry)