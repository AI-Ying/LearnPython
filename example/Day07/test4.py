#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-24 01:32:43
# Description : with上下文管理器


class Foo:
    """description"""
    def __enter__(self):
        """docstring for __enter__"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """docstring for __exit__"""
        print("exc_type:{0}".format(exc_type))
        print("exc_val:{0}".format(exc_val))
        print("exc_tb:{0}".format(exc_tb))


if __name__ == '__main__':
    with Foo() as foo:
        print("hello with!")
        a = 1 / 0
        print("end with!")
