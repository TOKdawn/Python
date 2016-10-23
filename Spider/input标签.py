#!/usr/bin/python

import lxml.html
import pprint
import urllib2
def parse_form(html):
      tree = lxml.html.fromstring(html)
      data = {}
      for e in tree.cssselect('form input'):
            if e.get('name'):
                  data[e.get('name')] = e.get('value')
      return data
url = 'https://sso.neusoft.edu.cn/authorize?response_type=code&client_id=e&redirect_uri=https%3A%2F%2Fe.neusoft.edu.cn%2Fwww%2Fsignin&scope=get_user_account&state=C6qIjuy5r99z1PrNfmewi1sV842AiK'
html = urllib2.urlopen(url).read()
form = parse_form(html)
pprint.pprint(form)
