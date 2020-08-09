import requests
res=requests.get('https://ichef.bbci.co.uk/news/320/cpsprodpb/2377/production/_106997090_bang_theory_reuters.jpg')
with open('big_bang_cast.jpg','wb') as rf:
     rf.write(res.content)