#!/usr/bin/python

import re
f = open('/Users/dawn/zpy/aaa.txt')
string = f.read()
pe_one = re.compile(r'(<td>|<br>)(\s*.*)')
ruest_list = pe_one.findall(string)
#ruext = pe_one.search(string)
#print ruext.group()
for x in ruest_list:
	print(x)