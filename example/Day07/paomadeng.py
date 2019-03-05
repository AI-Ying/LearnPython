#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-03-05 18:27:44
# Description : 跑马灯文字

import os
import time


def main():
    content = '好好学习，天天向上'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
