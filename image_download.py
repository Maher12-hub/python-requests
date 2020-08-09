import requests
res=requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png','wb') as rf:
        rf.write(res.content)