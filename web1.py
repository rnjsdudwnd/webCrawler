import requests
from bs4 import BeautifulSoup
r=requests.get("http://news.naver.com./main/list.nhn?mode=LSD&mid=sec&sid1=100")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find("ul",{"class":"type06_headline"})
all2=all.find_all("li")
for item in all2:
    title=item.find("dt",{"class":""}).text.replace("\t","").replace("\n","")
    modifyTitle=title[2:len(title)+1]
    #[2:5] ->2,3,4
    print(modifyTitle)
    
