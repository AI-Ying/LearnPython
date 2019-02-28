#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-28 22:06:55
# Description : templates

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    """docstring for index"""
    data = {
        'name': 'ai',
        'age': 18,
        'my_dic': {'city': 'Beijing'},
        'my_list': [1, 2, 3, 4, 5],
        'my_int': 0,
    }
    # return render_template('index.html', name='ai', age=18)
    # data前面的**表示按键-值对解析字典
    return render_template('index.html', **data)


# 自定义过滤器方法一
def list_split2(li):
    """自定义过滤器方法一 list_split2"""
    return li[::2]


# 注册过滤器
app.add_template_filter(list_split2, 'lis2')


# 自定义过滤器方法二
@app.template_filter('lis3')
def list_split3(li):
    """自定义过滤器方法一 list_split2"""
    return li[::3]
