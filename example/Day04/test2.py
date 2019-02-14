#!/usr/bin/python6
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2020-02-14 12:43:35
# Description : 判断一个数是不是素数(质数)


from math import sqrt

num = int(input("输入一个数："))
end = int(sqrt(num))+1
is_prime = True
for x in range(2, end):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print("{0}是素数".format(num))
else:
    print("{0}不是素数".format(num))
