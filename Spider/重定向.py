#!/usr/bin/python

#https://e.neusoft.edu.cn/www/signin
# -*- coding:UTF-8 -*-

from urllib2 import Request,urlopen,URLError,HTTPError

old_url = 'http://e.neusoft.edu.cn/www/signin'
req = Request(old_url)
response = urlopen(req)
print 'Old url: ' + old_url
print 'Peal url: ' + response.geturl()