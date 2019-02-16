#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-14 21:34:47
# Description : 水仙花


num = int(input("输入数字: "))

num_length = len(str(num))
count = num_length
num_sum = 0
while count:
    num_sum += (((num // (10 ** (count- 1))) % 10) ** num_length)
    count -= 1
else:
    if num_sum == num:
        print(True)
    else:
        print(False)
