import requests
import os
import webbrowser as wb
url='https://www.youtube.com/results?search_query=how+we+can+activate+the+conda+environment'
res=requests.get(url)
with open('youtube.html','w',encoding='utf-8') as wf:
    wf.write(res.text)
file_path=os.path.realpath('youtube.html')
wb.open(file_path)