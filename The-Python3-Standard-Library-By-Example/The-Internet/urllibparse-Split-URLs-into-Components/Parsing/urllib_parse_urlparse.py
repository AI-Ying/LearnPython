# -*- coding: utf-8 -*-

# urlparse() 返回一个tupe, tupe不同于list, tupe元素不能修改且使用()
from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)



