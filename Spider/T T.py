#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#/Users/dawn/Library/Application Support/Firefox/Profiles/cv2d3zgc.default #coolie路径
import urllib2
import urllib
import cookielib
import lxml.html
import pprint  
def parse_form(html):
	tree = lxml.html.fromstring(html)
	data = {}
	for e in tree.cssselect('form input'):
		if e.get('name'):
			data[e.get('name')] = e.get('value')
	return data
url = 'https://sso.neusoft.edu.cn/authorize?response_type=code&client_id=e&redirect_uri=https%3A%2F%2Fe.neusoft.edu.cn%2Fwww%2Fsignin&scope=get_user_account&state=C6qIjuy5r99z1PrNfmewi1sV842AiK'
LOGIN_NAME = 'zhangpengyu15'
LOGIN_PASS = '383409'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(url).read()
data = parse_form(html)
data['username'] = LOGIN_NAME
data['password'] = LOGIN_PASS

encode_data = urllib.urlencode(data)
request = urllib2.Request(url,encode_data)
response=urllib2.urlopen(request)
print response
#response = opener.open(request)
#response.geturl()