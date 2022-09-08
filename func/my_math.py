from asyncio.windows_events import NULL
from cmath import sqrt
import math
from typing import Iterable


def _abx(x):
    if not isinstance(x, (int, float)):
        return 0
    if x > 0:
        return x
    else:
        return -x


def _quadratic(a, b, c):
    _absB = abs(math.sqrt(math.pow(b, 2)-4*a*c))
    x1 = (-b+_absB)/(2*a)
    x2 = (-b-_absB)/(2*a)
    return x1, x2


def _square_numbers1(numbers):
    sum = 0
    for num in numbers:
        sum += num*num
    return sum


# 可变参数
def _square_numbers2(*numbers):
    sum = 0
    for num in numbers:
        sum += num*num
    return sum


def _move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        _move(n-1, a, c, b)
        print(a, '->', c)
        _move(n-1, b, a, c)


def _move_2(n, a, b, c):
    while n > 0:
        n -= 1
        print(a, '->', c)
        print(a, '->', b)
        print(c, '->', b)
        print(a, '->', c)


def findMinAndMax(L):
    if L:
        return min(L), max(L)
    else:
        return (None, None)


def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        n += 1
        a, b = b, b+a


# 求积
def prod(x, y):
    return x*y


# 闭包返回递增函数
def createCounter():
    x = 0

    def fn():
        nonlocal x
        x = x+1
        return x
    return fn
