import requests

payload={'key1':'value1'}
res=requests.post('https://httpbin.org/post',data=payload)
print(res.text)