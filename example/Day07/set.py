#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-03-05 16:03:08
# Description : 集合


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('length == {0}'.format(len(set1)))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(5)
    set1.add(6)
    print(set1)
    set2.update([11, 12])
    print(set2)
    set2.discard(5)
    print(set2)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    for e in set2:
        print(e ** 2, end=' ')
    print()
    set3 = set((1, 2, 3, 4, 5, 6))
    print(set3)
    print(set3.pop())
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)
    print(set1 <= set2)
    print(set1 >= set2)


if __name__ == '__main__':
    main()
