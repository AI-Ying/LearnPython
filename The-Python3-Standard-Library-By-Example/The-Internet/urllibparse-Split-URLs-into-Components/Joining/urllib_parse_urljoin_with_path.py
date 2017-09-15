# -*- coding: utf-8 -*-

# 如果被join的路径中开始含有slash(/)，那么会resets原来的URL，
# 如果开始处不含有slash(/), 那么会直接在URL后面添加路径
from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/',
        '/subpath/file.html'))
print(urljoin('http://www.example.com/path/',
        'subpath/file.html'))

