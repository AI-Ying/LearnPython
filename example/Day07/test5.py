#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-26 23:53:53
# Description : 元组


def main():
    tupe = ('python', True, 18)
    print(tupe)

    print(tupe[1])
    print(tupe[2])

    for t in tupe:
        print(t)

    # tupe[0] = 'flask'
    tupe = ('flask', False, 20)
    print(tupe)

    # 将元组转换成列表
    list_of_tupe = list(tupe)
    print(list_of_tupe)

    # 将列表转换成元组
    fruits = ['apple', 'orange', 'banana']
    tuple_of_list = tuple(fruits)
    print(tuple_of_list)


if __name__ == '__main__':
    main()
