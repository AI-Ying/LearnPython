# -*- coding: utf-8 -*-

# 把查询字符串分成dict(parse_qs)或者tupe(parse_qsl)
from urllib.parse import parse_qs, parse_qsl

encoded = 'foo=foo1&foo=foo2'

print('parse_qs :', parse_qs(encoded))
print('parse_qsl:', parse_qsl(encoded))


