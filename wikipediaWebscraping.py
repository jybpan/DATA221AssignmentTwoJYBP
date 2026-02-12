import requests
from bs4 import BeautifulSoup as bs4 

header = {"User-Agent": "DataSciAssignmentScraper/1.0 benjamin.pan1@ucalgary.ca"}

webRequest = requests.get('https://en.wikipedia.org/wiki/Data_science', headers=header)
html = bs4(webRequest.text, 'html.parser')

pageTitle = html.title.get_text(strip=True)
print(pageTitle)

contentText = html.find('div', id='mw-content-text')

fistParagraph = ""

if contentText is not None:
    paragraphs = contentText.find_all('p')

    for paragraph in paragraphs:
        paragraphText = paragraph.get_text(strip=True)

        if len(paragraphText) >= 50:
            firstParagraph = paragraphText
            break

print(f"The first paragraph with more than 50 characters is\n\n{firstParagraph}")