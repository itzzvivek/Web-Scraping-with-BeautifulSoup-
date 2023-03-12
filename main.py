# Note for webscraping in python by beautifysoup

# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# step 0 : Install all the requirements 
# pip install request
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#step 1 : Get the html
r = requests.get(url)
htmlContent = r.content

# print(htmlContent)

# step 2 : Parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# commonly used type of objects
#print(type(title)) #1. Tag 
#print(type(title.string))#2. NavigableString
#print(type(soup))#3. BeautifulSoup
#4. Comments 
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.string))
# exit()

# get the title of the html page
# title = soup.title

#get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

#get first elements
# print(soup.find('p'))

#get class of any html in the page
# print(soup.find('p')['class'])
# print(soup.find('p')['id'])

#find all the elements with class lead
# print(soup.find_all('p',class_="lead"))

#get the text from the tags/soup

# print(soup.find('p').get_text())

#get all text from html page
# print(soup.get_text())

#get all the anchor from the page
anchors = soup.find_all('a')
all_links =set()
# print(anchors)

#get all the links on the page:
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = "https://codewithharry.com" +link.get('href')
#         all_links.add(link)
#         print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent)
# print(navbarSupportedContent.contents)
for elem in navbarSupportedContent.children:
    # print(elem)

#.content- A tag's children are available as a list
#.children - A tag's children are available as a generator

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)