from bs4 import BeautifulSoup as bs
import requests
import re
url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
page = requests.get(url)
# print(page.status_code)
soup = bs(page.content, 'html.parser')
# print(soup.prettify())

pdfs = soup.find_all(href=re.compile(".pdf"))
print(pdfs[:2])
print(pdfs[0]['href'])

list_of_pdf = set()
for pdf in pdfs:
    
    list_of_pdf.add(pdf['href'])
    
print(list_of_pdf)