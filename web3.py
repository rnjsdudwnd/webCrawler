import requests, operator, pandas,glob2
from bs4 import BeautifulSoup
from datetime import datetime

def crawling(date, pageCount):
    now=datetime.now()
    l=[]

    for i in range(1,int(pageCount)):
        r= requests.get("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100&date=" +str(date) + "page=")
        c= r.content
        soup=BeautifulSoup(c, "html.parser")
        #print(soup)
        all=soup.find("ul",{"class":"type06_headline"})
        all2=all.find_all("li")
        for item in all2:
            d={}
            try:
                title=item.find("dt",{"class":""}).find("a")
                links=item.find("dt",{"class":""}).find("a")['href']
                d["title"]=title
                d["links"]=links
            except:
                d["title"]="None"
                d["links"]="None"

            try:
                img=item.find("dt",{"class":"photo"}).find("img")['src']
                d["imgSrc"]=img
            except:
                d["imgSrc"]="None"

            l.append(d)
    df=pandas.DataFrame(l)
    df.to_csv('%s-%s-%s-%s-%s-%s.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second))



def loadFile(fileName):
    outputFileName=checkFileName(fileName)
    if outputFileName is not -1:
        df = pandas.read_csv(outputFileName)
        content=df["Content"]
        title=df["Title"]
        company=df["Company"]
        print(title)
        print("csv File Load Success")
    else:
        print("Error csv File")

def checkFileName(fileName):
    now=datetime.now()
    if len(glob2.glob("*.csv"))==0:
        print("No file found in this directoty")
        return -1
    else:
        if fileName =="all":
            result=[]
            for i in glob2.glob("*.csv"):
                result.append(pandas.read_csv(i))
            outputFileName = '%s-%s-%s-%s-%s-%s merging.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
            resultDf=pandas.concat(result, ignore_index=True)
            resultDf.to_csv(outputFileName, encoding='utf-8-sig')
            return outputFileName
        else:
            return fileName

def mainSetting():
    while(1):
        kb=input("$ TYPE CRAWLING NOW ")
        if kb is "exit":
            break
        elif kb == "crawling":
            date=input("Enter news date: ")
            pageCount=input("Enter pagecount : ")
            crawling(date, pageCount)
        elif kb == "loadAll":
            checkFileName("all")
        elif kb == "load":
            fileName=input("Enter csv FileName : ")
            loadFile(fileName)
        else:
            print("Error command")

mainSetting()