# -*- coding: utf-8 -*-

from urllib.parse import quote, quote_plus, urlencode

url = 'http://localhost:8080/~hellomann/中文'
print('urllencode() :', urlencode({'url' : url}))
print('quote()      :', quote(url))
print('quote_plus   :', quote_plus(url))


