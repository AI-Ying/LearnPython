#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-16 19:02:14
# Description : craps赌博游戏

import random

flag = True
flag_two = True
while flag:
    times = 0
    one = int(6*random.random())+1
    two = int(6*random.random())+1
    value = one + two
    times += 1
    if value == 7 or value == 11:
        print("玩家胜-完了{0}几次；筛子一：{1}  筛子二：{2}".format(times, one, two))
        flag = False
    elif value == 2 or value == 3 or value == 12:
        print("庄家胜-完了{0}几次；筛子一：{1}  筛子二：{2}".format(times, one, two))
        flag = False
    else:
        while flag_two:
            one_se = int(6*random.random())+1
            two_se = int(6*random.random())+1
            value_se = one_se + two_se
            times += 1
            if value_se == value:
                print("玩家胜-完了{0}几次；筛子一：{1}  筛子二：{2}".format(times, one, two))
                flag_two = False
                flag = False
            elif value_se == 7:
                print("庄家胜-完了{0}几次；筛子一：{1}  筛子二：{2}".format(times, one, two))
                flag_two = False
                flag = False
            else:
                continue
