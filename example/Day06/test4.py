#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 16:30:09
# Description : 判断一个数是否是回文素数


from test2 import palindrom_number
from test3 import preme


def palindrom_preme(num):
    """docstring for palindrom_preme"""
    if palindrom_number(num) and preme(num):
        return True
    return False


if __name__ == '__main__':
    num = int(input("请输入数字："))
    if palindrom_preme:
        print("{0}是回文素数".format(num))
