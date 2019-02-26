#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 19:07:49
# Description : 列表的使用

import sys


def main():
    """docstring for main"""
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello']*5
    print(list2)
    print(len(list2))
    print(list1[0])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    list1[2] = 200
    print(list1)
    list1.append(300)
    list1.insert(2, 400)
    list1 += [1000, 2000]
    print(list1)
    list1.remove(7)
    print(list1)
    if 3 in list1:
        list1.remove(3)
    print(list1)
    del list1[0]
    print(list1)

    list1.clear()
    print(list1)

    # 切片
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()

    fruits2 = fruits[:]
    print(fruits2)
    fruits3 = fruits2[::-1]
    print(fruits3)

    fruits4 = sorted(fruits)
    fruits5 = sorted(fruits, reverse=True)
    print(fruits)
    print(fruits4)
    print(fruits5)

    fruits6 = sorted(fruits, key=len)
    print(fruits6)
    fruits.sort(reverse=True)
    print(fruits)

    # 创建列表
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDEF' for y in '1234567']
    print(f)
    f = [x ** 2 for x in range(1, 10)]
    print(f)
    print(sys.getsizeof(f))

    # 使用生成器,不占用数据存储空间
    # 也可以使用yield关键字改造成生成器函数
    f = (x ** 2 for x in range(1, 10))
    print(f)
    print(sys.getsizeof(f))

    for var in f:
        print(var, end=' ')

    print()

    for val in fib(20):
        print(val, end=' ')


# 使用yield关键字列表生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    main()
