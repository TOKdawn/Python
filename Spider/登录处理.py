#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import urllib2
import cookielib
import cookielib
import urllib

url = 'https://sso.neusoft.edu.cn/authorize?response_type=code&client_id=e&redirect_uri=https%3A%2F%2Fe.neusoft.edu.cn%2Fwww%2Fsignin&scope=get_user_account&state=C6qIjuy5r99z1PrNfmewi1sV842AiK'
LOGIN_NAME = 'zhangpengyu15'
LOGIN_PASS = '383409'
data = {'username' : LOGIN_NAME,'password' : LOGIN_PASS}
encoded_data = urllib.urlencode(data)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
opener = urllib2.urlopen(url)
opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')]
print response.getcode()
print cj
print response.read()