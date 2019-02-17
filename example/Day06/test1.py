#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 13:38:42
# Description : 函数实现最大公约数和最小公倍数


def gcd(num1, num2):
    """
    gcd:最大公约数
    num1, num2:参数
    """
    if num1 > num2:
        (num1, num2) = (num2, num1)

    for factor in range(num1, 0, -1):
        if num2 % factor == 0 and num1 % factor == 0:
            return factor


def lcf(num1, num2):
    """
    lcf:最小公倍数
    num1, num2:参数
    """
    lcf = num1 * num2 // gcd(num1, num2)
    return lcf
