# -*- coding: utf-8 -*-

# 把编码后的参数添加到URL中，并访问
from urllib import parse
from urllib import request

query_args = {'q': 'query string', 'foo':'bar'}
encoded_args = parse = parse.urlencode(query_args)
print('Encoded', encoded_args)

url = 'http://localhost:8080/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))
