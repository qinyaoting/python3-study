#!/usr/bin/python3

# OOP



class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def print_score(self):
        print('%s:%s' % (self.name, self.score))



if __name__ == '__main__':
    bart  =Student('bob', 44)
    lisa  =Student('Lisa', 88)
    bart.print_score()
    lisa.print_score()


    # 测试模块和类的区别
    # import fish
    # fish.fishing()

    from lxf.fish import *
    bb = GoldenFish()
    bb.swim()

