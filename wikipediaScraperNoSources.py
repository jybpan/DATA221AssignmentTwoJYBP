import requests
from bs4 import BeautifulSoup as bs4 

header = {"User-Agent": "DataSciAssignmentScraper/1.0 benjamin.pan1@ucalgary.ca"}

webRequest = requests.get('https://en.wikipedia.org/wiki/Data_science', headers=header)
html = bs4(webRequest.text, 'html.parser')


contentText = html.find("div", id="mw-content-text")

prohibitedWords = ["references", "external links", "see also", "notes"]
heading = []

for h2Tag in contentText.find_all('h2'):
    headlineSpan = h2Tag.find("span", class_="mw-headline")
    if headlineSpan is None:
        headingText = h2Tag.get_text(separator=" ", strip=True)
    else:
        headingText = headlineSpan.get_text(strip=True)

    headingLowered = headingText.lower()

    shouldSkipHeading = False

    for word in prohibitedWords:
        if word in headingLowered:
            shouldSkipHeading = True
            break

    if not shouldSkipHeading and headingText:
        heading.append(headingText)

with open("headings.txt", "w", encoding="utf-8") as file:
    for extractedHeadings in heading:
        file.write(extractedHeadings + "\n")