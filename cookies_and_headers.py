import requests
#url='https://httpbin.org/cookies'
#res=requests.get(url)
#print(res.cookies)
url='https://httpbin.org/headers'
res=requests.get(url)
print(res.headers)