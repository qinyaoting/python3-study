#!/usr/bin/python3

# 统计文件中的某个单词的频率


# V1
def count1():
    text_file = open('./animal_data', 'r')
    dog_count = 0
    cat_count = 0

    for line in text_file.readlines():
        for word in line.split():
            word = word.lower()
            if word == 'dog':
                dog_count = dog_count + 1

    print('the word dog occurs', dog_count)

# V2


'''
Content of file:

Hi this is hello
Hello is my name
Then

text_file.read()
will give,

['Hi this is hello\n', 'Hello is my name\n']

text_file.read().splitlines()
['Hi this is hello', 'Hello is my name']
Then split every line in your lines,

lines = map(str.split,text_file.read().splitlines())
[['Hi', 'this', 'is', 'hello'], ['Hello', 'is', 'my', 'name']]
On chaining the iterable,

it.chain.from_iterable(map(str.split,text_file.read().splitlines()))
['Hi', 'this', 'is', 'hello', 'Hello', 'is', 'my', 'name']
And,

search=['dog','cat'] # the words that you need count
search = dict.fromkeys(search,0) # will give a dict as {'dog':0,'cat':0}

'''


def count2():
    text_file = open("./animal_data", 'r')
    search = ['cat', 'dog']
    # 从list构造dict, 奇特
    search = dict.fromkeys(search, 0)
    import itertools as it
    # res = dict()
    # from_iterable的作用是拍扁, map第一个方法是怎么处理后边字符串的方法
    for word in it.chain.from_iterable(map(str.split, text_file.read().splitlines())):
        if word.lower() in search:
            search[word.lower()] = search[word.lower()] + 1

    for word, count in search.items():
        print('the word %s occurs %d times' % (word,count))


if __name__ == '__main__':
    count1()
    count2()
