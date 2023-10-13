import math


def calculate(x):
    a = 1 + math.e ** -x
    b = 1 / a
    print(b)


x = int(input("x = "))

calculate(x)
