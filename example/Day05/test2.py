#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-16 12:55:01
# Description : 完美数


num = int(input("输入一个数字："))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("{0}是完美数".format(num))
else:
    print("{0}不是完美数".format(num))



