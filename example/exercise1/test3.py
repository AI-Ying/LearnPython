#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author : Arthur Yan
# Date   : 2019-02-06 15:54:00

year = int(input("Input year"))
is_leap = (year % 4 == 0 and year % 100 == 0 or
    year % 400 == 0)
print(is_leap)
