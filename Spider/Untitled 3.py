#!/usr/bin/python
#--*-- coding:utf-8 --*--
import urllib,urllib2
num = 1
#url = 'https://e.neusoft.edu.cn/manager/user/?page='+num
url = 'https://e.neusoft.edu.cn/shop'
_headers = { "Host": "e.neusoft.edu.cn",
            'Cookie': 'xK8gtasdpydSum7G93y4jwrKR8VtrXjx,0ks2g6corhlew58btvow94v7yco5rzzk',
            'Connection':'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=9.0,image/webp,*/*; q=0.8',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
            'DNT':'1',
            'Referer': 'https://e.neusoft.edu.cn/manager/user/',
            'Accept-Encoding': 'gzip, deflate, sdch,br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-GB;q=0.6,en;q=0.4'
            }
data = None
req = urllib2.Request(url, headers=_headers)
try:
      html = urllib2.urlopen(req).read()
except urllib2.URLError as e:
      print 'Download error:',e.reason
response = urllib2.urlopen(req)
compressedData = response.read()
print compressedData