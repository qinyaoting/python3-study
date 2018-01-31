#!/usr/bin/python3

# n!
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("1! = %d" % fact(1))
print("5! = %d" % fact(5))
print("100!=%d" % fact(100))

# print(fact(1000))
# RecursionError: maximum recursion depth exceeded in comparison

