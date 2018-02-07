#!/usr/bin/python3
from http import cookiejar
from urllib import request

def save_cookie_into_file(url):
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    # cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(url)
    for item in cookie:
        print('Name = %s' % item.name)
        print('value = %s' % item.value)
    cookie.save(ignore_discard=True, ignore_expires=True)

def read_cookie_from_file():
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print('saved cookie:' , response.read().decode('utf-8'))

if __name__ == '__main__':
    save_cookie_into_file('http://www.baidu.com')
    read_cookie_from_file()
