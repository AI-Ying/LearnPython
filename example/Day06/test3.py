#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 15:04:21
# Description : 判断一个数是否是素数


from math import sqrt


def preme(num):
    """docstring for preme"""
    if num != 1:
        end = int(sqrt(num))+1
        for i in range(2, end):
            if num % i == 0 and num != 1:
                return True
    return False


re = preme(4)
print(re)
