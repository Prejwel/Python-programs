import requests

payloadget={'page':2,'count':25}
payloadpost={'username':'Prejwel','password':'testing'}
# -------- to get some data with url we need to use ( get , url, param= )
#---- to post some data to url we need to use (post, url , data= )

# r=requests.get('https://httpbin.org/get',params=payloadget)
# print(r.text)
# r.url   #-> The URL with the parameters will be shown

p = requests.post('https://httpbin.org/post',data=payloadpost)
print(p.text)
