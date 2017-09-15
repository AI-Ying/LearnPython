# -*- coding: utf-8 -*-

# 把一些非标准的字符转化成标准的URL字符
# 参数通过key=value成对出现，参数之间使用&连接
from urllib.parse import urlencode

query_args = {
        'q' : 'query string',
        'foo': 'bar',
        'zh': '中文',
}
encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)

