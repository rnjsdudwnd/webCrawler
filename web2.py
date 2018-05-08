import requests
from bs4 import BeautifulSoup
r=requests.get("http://news.naver.com./main/list.nhn?mode=LSD&mid=sec&sid1=100")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find("ul",{"class":"type06_headline"})
all2=all.find_all("li")

for item in all2:
    #title=item.find("dt", {"class":""}).text.replace("\t","").replace("\n","")
    #modifyTitle=title[2:len(title)+1]
    #print(modifyTitle)
    try:
        img= item.find("dt",{"class":"photo"})
        img2=img.find("img")["src"]
        print(img2)
    except:
        print("No image")
        
        
