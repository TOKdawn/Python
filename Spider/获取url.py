#!/usr/bin/python
#-*- coding: UTF-8 -*- 
import re
import urllib
import urllib2
def download (url,user_agent='wawp',num_restries=2):
	#print 'Download:',url
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url,headers=headers)
	#print request
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:',e.reason
		html = None
		if num_restries >0:
			if hasattr(e,'code') and 500<=e.code<600:
				# retry 5XX HTTP errors
				return download(url,user_agent,num_retries-1)
	return html
url = 'https://e.neusoft.edu.cn/www/signin'
login_url_undispose = download(url)
#print login_url_undispose
pa = re.compile(r'URL=.*\s\/\>')
ma = pa.search(login_url_undispose)
#print ma.group()
(b,c)= ma.span()
login_url_dispose = login_url_undispose[b+4:c-4]
print login_url_dispose
