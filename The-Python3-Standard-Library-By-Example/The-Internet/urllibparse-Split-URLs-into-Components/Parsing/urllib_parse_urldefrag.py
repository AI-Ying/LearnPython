# -*- coding: utf-8 -*-

# urldefrag()把一个复合的URL分成url+fragment, 简化复合的URL
from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('original:', original)
d = urldefrag(original)
print('url:', d.url)
print('fragment:', d.fragment)

