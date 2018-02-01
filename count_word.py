#!/usr/bin/python3

'''
try:
    f = open("./data", 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''

'''
统计词频, V1
用空格分割单词


'''
with open("./data", 'r') as f:

    dict = {}

    lines = f.readlines()

    for line in lines:
        # 去掉行尾的空白, 用空格分割
        words = line.strip().split(" ")

        for word in words:
            if word in dict:
                count = dict[word]
                dict[word] = count+1
            else:
                dict[word] = 1



    print(dict)



'''
统计词频v2
'''
try:
    file = open("./data")
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for k, v in wordcount.items():
        print(k, v)


finally:
    file.close()
'''

统计词频v3
'''
'''

统计词频v4
'''
