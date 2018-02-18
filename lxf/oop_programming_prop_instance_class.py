#!/usr/bin/python3

# 实例属性类属性



class Student(object):

    # 类属性
    name = "Student"
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    s = Student('Bob')
    print(s.name)
    print(Student.name)
    del s.name
    print(s.name)

'''
实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''