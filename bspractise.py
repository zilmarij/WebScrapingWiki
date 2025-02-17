html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""
from bs4 import BeautifulSoup as bs
soup = bs(html_doc, 'html.parser')

# Going down the tree:



#Navigating using tag names: find() method, find_all() method:
# print(soup.find('head')) #OR 
# print(soup.head.title)
# print(soup.find_all('a'))


#tag's direct children using .contents and .children
# print(soup.head.contents[0].contents)
# print(soup.body.contents[3].contents[0])
# for child in soup.body.children:
#     print(child)
    
#The .descendants attribute: to iterate over all of a tag's children grandchildren.., recursively
# for desc in soup.body.descendants:
#     print(desc)

# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

#print(soup.head.string) #bec. head has only child which is a navigablestr
#print(soup.body.p.string)
#.strings generator: to see all descendant strings
# for strs in soup.body.strings:
#     print(strs)
#.stripped_strings generator: remove extra whitespace by using 
# for strs in soup.body.stripped_strings:
#     print(strs)
    
    
#Going up the tree:
#.parent: to get the parent of a tag
# print(soup.title.parent)
# #parent of tag string is the tag itself
# print(soup.title.string.parent)
# #parent of top-level tag is the bs object itself
# print(soup.html.parent)  
# #parent of bs obj is None:
# print(soup.parent)

# .parents: iterate over all of an element's parents
# aTag = soup.a
# print(aTag)
# for parent in aTag.parents:
#     print(parent.name)
#.self_and_parents generator: gives the entire ancestry of an element, including the element itself


