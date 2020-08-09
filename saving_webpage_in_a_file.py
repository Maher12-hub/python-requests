import requests
import os
import webbrowser as wb
url='https://dimikcomputing.com'
res=requests.get(url)
with open('dimik.html','w',encoding='utf-8') as wf:
    wf.write(res.text)
file_path=os.path.realpath('dimik.html')
wb.open(file_path)