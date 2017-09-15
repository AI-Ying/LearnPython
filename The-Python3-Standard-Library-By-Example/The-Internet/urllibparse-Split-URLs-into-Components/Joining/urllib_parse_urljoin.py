# -*- coding: utf-8 -*-

# 使用相对路径或者绝对路径替换
from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/file.html',
        'anotherfile.html'))
print(urljoin('http://www.example.com/path/file.html',
        '../anotherfile.html'))

