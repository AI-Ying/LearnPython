# -*- coding: utf-8 -*-

import urllib2
import random

# URL 统一资源定位符
# 协议类型:[//服务器地址[:端口号]][/路径]文件名[?查询][#片段]
# urlopen(url, data, timeout)
# url:URL data:访问URL时要传送的数据 timeout:设置超时时间
# Return 一个对象

'''
response = urllib2.urlopen('http://www.baidu.com')
# 不加read直接打印出该对象的描述
#html = response
html = response.read()
print html
'''

# s = '-hello wrold-'
# s = '\n\t hello world'
# print s
# s.strip()函数
# s.strip(rm)  删除s字符串开头、结尾处，位于rm剔除序列的字符
# S = s.strip('-')
# s.lstrip(rm) 删除s字符串开头处，位于rm删除序列的字符
# S = s.lstrip('-')
# s.rstrip(rm) 删除s字符串中结尾处，位于rm删除序列的字符
# S = s.rstrip('-')
# s.strip()    默认删除空白符(包括'\n','\r',' ')
# S = s.strip()
# print S


# str.capitalize() 返回一个首字母大写的字符串
# s = 'hello world'
# S = s.capitalize()
# print S

# random.sample(sequence, k) 从指定序列中随机获取指定长度的片段,不会修改原序列
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# slice = random.sample(list, 5)
# print slice
# print list

# random.randint(a, b) 用于生成"一个"指定范围的整数。其中a是下限，b是上限
# print random.randint(5, 8)

# random.shuffle(list) 用于将一个列表中的元素打乱, 原列表的内容已改变
# lists = ['python', 'is', 'powerful', 'simple', 'and so on ...']
# random.shuffle(lists)
# print lists

# join() 用于将序列中的元素以指定的字符串连接成一个新的字符串
# str = '-'
# seq = ('a', 'b', 'c')
# print str.join(seq)

# str.count(s) 返回s在str中出现的次数
# s = "hello world"
# print s.count("l")




# 推荐如下这样写
# request = urllib2.Request("http://learncodethehardway.org/words.txt")
# response = urllib2.urlopen(request)
# WORDS = []
# for i in response:
    # WORDS.append(i) 对比
    # WORDS.append(i.strip())

# for 的用法
# class_names = [w.capitalize() for w in WORDS]
# print class_names

# 打印所有lists元素
# listsa = ['hello', 'world', 'ai', 'ying']
# listsb = ['print', 'list', 'dict']
# for lists in listsa, listsb:
# for lists in listsa + listab:
#     print lists[:]

# str.replace(old, new [,  max])
# old是将被替换的字符串，new是新字符串，max是可选，替换不超过max次
# strings = 'hello world ai ying hello world ai ying'
# print strings.replace('hello', 'world', 1)
# print strings.replace('hello', 'world')
# listsa = ['hello', 'world', 'ai', 'ying', 'hello', 'ai', 'ying']
# listsb = ['hello']
# for element in listsa:
#     listsb =  listsb.replace('hello', 'world')
# print listsb

dic = {'hello':'Hello', 'world':'World', 'ai':'AI'}
print dic
print dic.keys()
# print dic.values()

snippets = dic.keys()
random.shuffle(snippets)
print snippets

for snippet in snippets:
    phrase = dic[snippet]
    print snippet, phrase


