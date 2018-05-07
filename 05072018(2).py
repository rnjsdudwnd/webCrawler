import os;
import os.path;
import sys;

content_list = []
is_start = False


def ReadFile(file_path):
    fp = open(file_path, 'r', encoding='utf8')
    read_data = fp.read()

    return read_data


def GetFileList(folder_path):
    filelist = os.listdir(folder_path)
    return filelist;


def start():
    print("Searching Service Start..")
    folder_path = '/root/PycharmProjects/young/testdb.txt';
    file_list = GetFileList(folder_path)

    for file_path in file_list:
        content = ReadFile(folder_path + file_path)

        content_dic = dict()
        content_dic["content"] = content
        content_dic["filename"] = file_path

        content_list.append(content_dic)

    is_start = True;


def stop():
    print("Searching Service Stop..")
    is_start = False;
    sys.exit()


def clear():
    content_list = []
    print(str(len(content_list)))


def search(search_word):
    result_list = []

    index = 0;
    for content_dic in content_list:

        content = content_dic["content"]
        filename = content_dic["content"]

        result = content.rfind(search_word)

        if (result > 0):
            result_list.append(index);

        index = index + 1

    result_len = len(result_list)
    if (result_len == 0):
        print("Do no find")
    else:
        print("Find : " + str(result_len))
        for idx in result_list:
            print(content_list[result_list[idx]])


def Conversation(text):
    if (text == "1"):
        start()
    elif (text == "!stop"):
        stop()

    elif (text == "!clear"):
        clear()
    else:
        search(text)


if __name__ == '__main__':

    while True:
        text = input(">>")
        Conversation(text)

