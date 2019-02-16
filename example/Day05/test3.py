#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-16 15:50:14
# Description : 百钱百鸡

# cocks     1-5
# hens      1-3
# chickens  3-1
# cocks + hens + chickens = 100
# 5*cocks + 3*hens + 1/3*chickens =100

cocks = 100 // 5
hens = 100 // 3
chickens = 100


for cock in range(cocks):
    for hen in range(hens):
        for chicken in range(chickens):
            animal_sum = cock + hen + chicken
            price_sum = 5*cock + 3*hen + 1/3*chicken
            if (animal_sum == 100 and price_sum == 100):
                print("cocks:{0},hens:{1},chicken:{2}"
                      .format(cock, hen, chicken))
                continue
