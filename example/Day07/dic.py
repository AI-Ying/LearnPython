#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-03-05 17:41:04
# Description : 字典


def main():
    dic1 = {'tom': 23, 'pipi': 34, 'lieo': 46}
    print(dic1)
    print(dic1['tom'])
    print(dic1.keys())
    print(dic1.values())
    for elem in dic1:
        print('{0}, {1}'.format(elem, dic1[elem]), end=' ')
    print()
    dic1['tom'] = 89
    print(dic1['tom'])
    # 如果没有这个键值，可以设置默认值
    print(dic1.get('lili', 43))
    print(dic1.popitem())
    print(dic1)
    print(dic1.pop('pipi'))
    print(dic1)
    dic1.clear()
    print(dic1)


if __name__ == '__main__':
    main()
