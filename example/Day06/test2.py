#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 14:28:57
# Description : 检测一个数是否是回文数


def palindrom_number(num):
    """judge for palindrom_number"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


re = palindrom_number(12321)
print(re)
