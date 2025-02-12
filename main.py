import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())