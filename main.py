import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

#page download
page = requests.get(url)

#page scrape
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

#page parse

# print(soup.find_all('p'))
# print(soup.find_all('p')[0].get_text())

object = soup.find(id="mp-left")
items = object.find_all(class_="mp-h2")
result = items[0]
# print(result.prettify())

# print(soup.script.string)
# print(soup.find('script').string)
print(soup.find_all('script')[0].string)

# pTag= soup.p
# print(pTag.string)
# print(list(soup.children))

# f = soup.find(id='printfooter')   
# print(f)