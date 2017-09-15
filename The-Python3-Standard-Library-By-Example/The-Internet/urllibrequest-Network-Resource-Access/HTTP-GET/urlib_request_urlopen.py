# -*- coding: utf-8 -*-

from urllib import request

# response 是urlopen()返回的一个类对象
# 可以使用类对象中的info()访问这个对象的headers，使用read()或者readlines()访问data
response = request.urlopen('http://localhost:8080')
print('RESPONSE  :', response)
print('URL       :', response.geturl())

headers = response.info()
print('DATA      :', headers['date'])
print('HEADERS   :')
print('-----------')
print(headers)

data = response.read().decode('utf-8')
print('LENGTH   :', len(data))
print('DATA     :')
print('----------')
print(data)
