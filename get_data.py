import requests
payload={'page':2,'count':25}

res=requests.get('https://httpbin.org/get')
print(res.text)