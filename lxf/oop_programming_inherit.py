#!/usr/bin/python3

# 继承和多态


class Animal(object):
    def run(self):
        print('animal running...')


class Dog(Animal):
    def run(self):
        print('dog running.......')

    def eat(self):
        print('dog eating something.....')


class Cat(Animal):
    pass


if __name__ == '__main__':
    dog = Dog()
    dog.run()

    dog.eat()

    a = []
    print(isinstance(a, list))
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))

    # 鸭子类型, 奇特, 不要求严格的继承体系, 一个对象看起来像鸭子, 走起路来像鸭子, 那它就可以被看做是鸭子


