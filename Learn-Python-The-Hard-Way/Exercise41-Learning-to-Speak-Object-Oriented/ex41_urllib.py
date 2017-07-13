# -*- coding: utf-8 -*-

import urllib2

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

# 推荐如下这样写
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

