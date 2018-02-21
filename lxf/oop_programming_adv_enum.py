#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

# 枚举


# 自定义枚举类
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6






if __name__ == '__main__':
    from enum import Enum

    Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    print(Month.Jan)

    for name, member in Month.__members__.items():
        print(name, '=>', member,',',member.value)
    # 使用自定义枚举类
    print(Weekday.Sun)
    print(Weekday['Mon'])
    print(Weekday.Tue.value)
    print(Weekday(1))

    for name, member in Weekday.__members__.items():
        print(name,'->',member)
