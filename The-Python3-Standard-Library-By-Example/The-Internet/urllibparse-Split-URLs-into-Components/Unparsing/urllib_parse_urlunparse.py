# -*- coding: utf-8 -*-

# 把一个规则的tuple转换成URL
from urllib.parse import urlparse, urlunparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG   :', original)
parsed = urlparse(original)
print('PARSED :', type(parsed), parsed)
t = parsed[:]
print('TUPLE  :', type(t), t)
print('NEW    :', urlunparse(t))


