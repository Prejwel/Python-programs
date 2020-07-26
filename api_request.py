import requests

r = requests.get('https://www.google.com')

# print(help(r)) - will show the methods and attributes that can be accessed with the url. (Structered manner)

# print(dir(r)) # -> Attributes and methods that we can access within the response object will be shown / content of the webpage

print(r.status_code) #success or failure (200, 404, 301 etc )

# print(r.headers)
#print(r.text)  # convertion of URL to HTML format



map = requests.get('https://maps.google.co.in/maps?hl=en&tab=wl')
with open('gmapcontent.png','wb') as f:
    f.write(map.content) #this will write the contents of url to a file