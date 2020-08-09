import requests
url='https://httpbin.org/get'
res=requests.get(url)
print(res.text)