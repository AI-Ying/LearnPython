# -*- coding: utf-8 -*-

from urllib import parse
from urllib import request

query_args = {'q' : 'query', 'foo' : 'bar'}
encoded_args = parse.urlencode(query_args).encode('utf-8')
url = 'http://localhost:8080/'
print(request.urlopen(url, encoded_args).read().decode('utf-8'))
