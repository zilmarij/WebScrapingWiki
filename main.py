import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

#page download
page = requests.get(url)

#page scrape
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

#page parse
pTag= soup.p
# print(pTag.string)
# print(list(soup.children))

# print(soup.find_all('p'))

# return only text
# does not include HTML tags
print(soup.find_all('p')[0].get_text())

# print(soup.find_all(class_="mp-h2")[0])