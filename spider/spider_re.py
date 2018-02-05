#!/usr/bin/python3
import re

#compile
s = '111,222,aaa.bbb.ccc333,444ddd'
rule = r'\b\d+\b'
compiled_rule = re.compile(rule)
compiled_rule.findall(s)

# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())
# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))

line = 'Cats are smarter than dogs'
match_obj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if match_obj:
    print("matchobj.group():", match_obj.group())
    print("matchobj.group(1):", match_obj.group(1))
    print("matchobj.group(2):", match_obj.group(2))
else:
    print("No match!")


# search
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

line = "Cats are smarter than dogs"
search_obj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if search_obj:
    print("searchobj.group():", search_obj.group())
    print("searchobj.group(1):", search_obj.group(1))
    print("searchobj.group(2):", search_obj.group(2))
else:
    print("No match!")

# sub
phone = '2004-959-559 # This is Phone number'
num = re.sub(r'#.*$', '', phone)
print(num)


import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html)
print(bsobj.prettify())
images = bsobj.findAll("img", {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
