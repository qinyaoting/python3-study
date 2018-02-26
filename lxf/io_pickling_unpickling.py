#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from os import read

__author__ = 'chin'

# 序列化

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def stu2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }

def dict2stu(dic):
    return Student(dic['name'], dic['age'], dic['score'])

if __name__ == '__main__':
    # 把内存中的变量变成可存储的或传输的过程称为序列化
    # 序列化之后的内容就可以保存到磁盘, 或者在网络上传输到其他 机器上
    import pickle
    d = dict(name='bob', age = 20, score=80)
    pickle.dumps(d)


    # 把序列化后的内容保存到文件
    f = open('dump.txt','wb')
    pickle.dump(d, f)
    f.close()

    # 从文件中反序列化
    f2 = open('dump.txt', 'rb')
    d2 = pickle.load(f2)
    f2.close()
    print(d2)

    #json
    import json
    d3 = dict(name='bob', age=20, score=88)
    json.dumps(d3)

    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    json.loads(json_str)

    # 对象的实例化
    s = Student('tom', 22, 99)
    print(json.dumps(s, default=stu2dict))

    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2stu))
