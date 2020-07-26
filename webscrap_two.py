import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.in/stores/page/A2CBF012-185A-4168-8756-2EB2C31451EB?_encoding=UTF8&ingress=0&ref_=topnav_storetab_inappledevicessubnav&visitId=913e599e-2ae6-444f-9abe-eb3de3fe76f3')
content = r.content
soup = BeautifulSoup(content,'html.parser')
#print(soup.prettify())

images = soup.findAll('img')
print(images)
print(len(images))

cee=soup.findAll("div",class_="stores-page")
print(cee)