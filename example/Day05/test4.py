#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-16 17:00:03
# Description : 斐波那契数列

# F(n) = F(n-1) + F(n-2)
# 1, 1, 2, 3, 5, 8 ......


def fib(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        result = fib(num-1) + fib(num-2)
        return result

print(fib(20))
