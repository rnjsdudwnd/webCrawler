from pymongo import MongoClient
import simplejson , csv, operator, os
# connect with my localhost as 27017
client = MongoClient('localhost', 27017)
# youngdb is my own db name
db = client.youngdb


def main():
    while True:
        print("1. Subtract Information from MongoDB")
        print("2. Create cvs")
        print("3. exit")
        option = input("choose ")
        if option == "1":
            print("1. Rough datas")
            print("2. arranged datas")
            option2 = input("choose ")
            if option2 == "1":
                check("confirm")
            elif option2 == "2":
                arranged("guy")
            else:
                print("Error")

        elif option == "2":
            print("1.Sending to csv")
            print("2.Find Keyword")
            option3 = input("choose ")
            if option3 == "1":
                csvfile("csv")
            elif option3 =="2":
                csvfile2("csv2")
            else:
                print("Error")
        elif option == "3":
            return -1
        else:
            print("Error")


def check(datass):
    if datass == "confirm":
        collection = db.project2_webpage.find()
        count = 0
        for result in collection:
            print(count)
            print(result)
            count = count + 1

        # link = ""
        # collection2 = db.project2_webpage.find({}).count()
        # collection3 = db.tutorialv2_webpage_webpage.find({},{'outlinks':1, '_id':0}).pretty()
        # print(collection)
        # print(collection2)
        # print(collection3)
        # print(link)
        print("")
        print("This is Crawling Datas you have in MongoDB.")
        print("You can change the datas if you change.")
        collection_list = db.collection_names()
        print(collection_list)
        print("")
        print("This is total datas you have.")
        collection2 = db.project2_webpage.find({}).count()
        print(collection2)
        print("")

    else:
        datass


def arranged(hi):
    if hi == "guy":
        # collection = db.project2_webpage.find_raw_batches()
        # for results in collection:
        #     print(bson.decode_all(results))
        collection3 = db.project2_webpage.distinct("inlinks")
        count2 = 0
        for result2 in collection3:
            count2 = count2 + 1
            print(count2)
            print(result2)
    else:
        hi


def csvfile(now):
    collection4 = db.project2_webpage.distinct("inlinks")
    if now == "csv":
        f = open('testdb.csv', 'w')
        simplejson.dump([collection4],f)
        f.close()
    else:
        now

def csvfile2(now2):
    if now2 == "csv2":
        print("!!")
    else:
      now2


main()
