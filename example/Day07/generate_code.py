#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-03-05 20:52:09
# Description : 生成验证码

import random


def generate_code(code_len=4):
    """docstring for main"""

    all_charts = '0123456789abcdefghipqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_charts) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_charts[index]
    return code


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2, m1 = m1, x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total + date


def main():
    # code = generate_code()
    # print(code)
    # suffix = get_suffix('test.txt')
    # print(suffix)
    # x = [2, 3, 5, 7, 3, 4, 1]
    # m1, m2 = max2(x)
    # print(m1, m2)
    print(which_day(1994, 10, 16))


if __name__ == '__main__':
    main()
