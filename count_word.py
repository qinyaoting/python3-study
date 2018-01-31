#!/usr/bin/python3


try:
    f = open("./data", 'r')
    print(f.read())
finally:
    if f:
        f.close()


with open("./data", 'r') as f:
    print(f.read())



# 如果文件很大比如10G, 用f.read()会内存爆掉
