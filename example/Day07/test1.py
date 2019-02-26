#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-17 16:36:03
# Description : 字符串使用



def main():
    """docstring for main"""
    str1 = "hello, world!"
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())

    print(str1.find('or'))
    print(str1.find('ai'))
    # 若未查到，则报异常
    # print(str1.index('or'))
    # print(str1.index('ai'))

    print(str1.startswith("He"))  # 检查字符串以什么开始
    print(str1.startswith("hel"))
    print(str1.endswith('!'))  # 检查字符串以什么结尾

    # 将字符串以指定宽度居中，并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定宽度放右，并在左侧填充指定字符串
    print(str1.rjust(50, ' '))

    str2 = 'abc123456'
    # sequence[starting_index:ending_index:step]
    # ------------------------------------------
    # -----|-a-|-b-|-c-|-1-|-2-|-3-|-4-|-5-|-6-|
    # -下标| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
    # -下标|-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |
    # ------------------------------------------
    print(str2[2])
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])

    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否由字符串构成
    print(str2.isalpha())
    # 检查字符串是否由字符串和数字构成
    print(str2.isalnum())

    str3 = '  ai@ying.com '
    print(str3)
    # 获得字符串修剪两侧空格的拷贝
    print(str3.strip())


if __name__ == "__main__":
    main()
