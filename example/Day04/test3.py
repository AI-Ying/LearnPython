#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-14 14:00:36
# Description : 最大公约数和最小公倍数

# python3
# / 表示除法会有小数，而//表示整型除法

num1 = int(input("输入数字一："))
num2 = int(input("输入数字二："))

if num1 > num2:
    (num1, num2) = (num2, num1)

for factor in range(num1, 0, -1):
    if num1 % factor == 0 and num2 % factor == 0:
        print("{0}和{1}的最大公约数是{2}".format(num1, num2, factor))
        print("{0}和{1}的最小公倍数是{2}".format(num1, num2, num1*num2//factor))
        break


