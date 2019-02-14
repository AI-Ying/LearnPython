#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author : Arthur Yan
# Date   : 2019-02-14 11:27:31

for row in range(1, 10):
    for column in range(1, row+1):
        print("{0}*{1}={2}".format(column, row, row*column), end='\t')
    print()
