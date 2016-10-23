#-*- coding: UTF-8 -*- 
#!/usr/bin/python
#https://e.neusoft.edu.cn/www/signin
import re
html = '<!DOCTYPE html><meta http-equiv="refresh" content="1; URL=https://sso.neusoft.edu.cn/authorize?response_type=code&amp;client_id=e&amp;redirect_uri=https%3A%2F%2Fe.neusoft.edu.cn%2Fwww%2Fsignin&amp;scope=get_user_account&amp;state=2FlpkOfd3gpBW4EJwMFjTLqI7HzQtz" />正在接入统一身份认证平台'
print html.find('URL')
pa = re.compile(r'URL=.*\s\/\>')
ma = pa.search(html)
print ma.group()
(b,c)= ma.span()
print html[b+4:c-4]
