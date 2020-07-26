import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
r = requests.get(url)
content = r.content
#print(content)
soup = BeautifulSoup(content,'html.parser')
#print(soup.prettify())

#tree traversal
title = soup.title
print(title)
print(title.string) #-> will show the title in string format
#---------
anchors = soup.find_all('a')
print(anchors) # will print all the anchor tag
#----------
paras = soup.find_all('p')
print(paras)  # to print all the paragraphs
#------------
#DIFFERENCE
# find('p') -> the 1st para will be shown
#findall('p') -> all paragraphs will be shown
#-----------
print(soup.find('p')['class']) # from the 1st para the class will be filtered

print(soup.find_all("p",class_='lead')) # all the class with lead will be taken

print(soup.get_text)
#---------
alllinks=set()
for link in anchors:
    if link.get('href')!='#':
        linkText=link.get('href')
        alllinks.add(link)
        print(link)

