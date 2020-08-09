import requests
base_url='http://subeen.com/download'
url=base_url+'process.php'
info={'name':'subeen','email':'book@subeen.com','country':'bangladesh'}
res=requests.post(url,data=info)
with open('book.pdf','wb') as wf:
    wf.write(res.content)
