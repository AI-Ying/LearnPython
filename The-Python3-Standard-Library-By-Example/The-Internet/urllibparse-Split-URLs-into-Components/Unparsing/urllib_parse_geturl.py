# -*- coding: utf-8 -*-

# 将分割成的多个components组成一个单一字符串
# 注意：geturl()只能用于urlparse()和urlsplit()函数
from urllib.parse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG   :', original)
parsed = urlparse(original)
print('PARSED :', parsed.geturl())


