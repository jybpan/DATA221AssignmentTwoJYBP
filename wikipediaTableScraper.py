import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

header = {"User-Agent": "DataSciAssignmentScraper/1.0 benjamin.pan1@ucalgary.ca"}

def cleanCellText(tag):
    return tag.get_text(" ", strip=True)

def tableHeader(tableTag):
    headerCells = []
    for rowTag in tableTag.find_all("tr"):
        thTags = rowTag.find_all("th")
        tdTags = rowTag.find_all("td")
        if thTags and not tdTags:
            headerCells = [cleanCellText(th) for th in thTags]
            break
    return headerCells

def tableDataRows(tableTag):
    dataRows = []
    for rowTag in tableTag.find_all("tr"):
        tdTags = rowTag.find_all("td")
        if not tdTags:
            continue
        rowCells = [cleanCellText(td) for td in tdTags]
        dataRows.append(rowCells)
    return dataRows

webRequest = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=header)
webRequest.raise_for_status()

html = bs4(webRequest.text, "html.parser")
contentText = html.find("div", id="mw-content-text")

tables = contentText.find_all("table")
chosenHeader = None
chosenRows = None

for tableTag in tables:
    dataRows = tableDataRows(tableTag)
    if len(dataRows) >= 3:
        chosenHeader = tableHeader(tableTag)
        chosenRows = dataRows
        break

maxColumns = max(len(row) for row in chosenRows)

if chosenHeader:
    headers = chosenHeader[:]
else:
    headers = []

while len(headers) < maxColumns:
    headers.append(f"col{len(headers) + 1}")

paddedRows = []
for row in chosenRows:
    paddedRow = row[:]
    while len(paddedRow) < maxColumns:
        paddedRow.append("")
    if len(paddedRow) > maxColumns:
        paddedRow = paddedRow[:maxColumns]
    paddedRows.append(paddedRow)

df = pd.DataFrame(paddedRows, columns=headers)
df.to_csv("wiki_table.csv", index=False)

print(f"Saved {len(df)} rows x {len(df.columns)} cols to wiki_table.csv!")