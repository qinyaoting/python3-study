#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

__author__ = 'chin'

try:
    from urllib.parse import parse_qs
except ImportError:
    # from urlparse import parse_qs
    pass


VALID_IPv4_SEGMENTS = [str(i).encode("latin1") for i in range(0x100)]
VALID_IPv6_SEGMENT_CHARS = b"0123456789abcdef"


def is_ipv4_address(string):
    if not isinstance(string, bytes):
        string = str(string).encode("latin1")
    segments = string.split(b".")
    # 拆分后的segment长度是4, 并且每个segment都是合法的
    return len(segments) == 4 and all(segment in VALID_IPv4_SEGMENTS for segment in segments)


def is_ipv6_address(string):
    if not isinstance(string, bytes):
        string = str(string).encode("latin1")
    segments = string.lower().split(b":")
    # 长度介于3到8, segment中每个字符都是合法的, 嵌套循环
    return 3 <= len(segments) <= 8 and all(all(c in VALID_IPv6_SEGMENT_CHARS for c in segment) for segment in segments)


def is_ip_address(string):
    return is_ipv4_address(string) or is_ipv6_address(string)


if __name__ == '__main__':

    # ip地址 192.168.0.1 - 192.168.0.255
    # 生成ip地址的各个部分比如 ['0','1',...'255']
    # 十六进制的100=十进制的256
    # encode把字符串变成bytes类型
    print([str(i).encode("latin1") for i in range(0x100)])

    print(isinstance('str',bytes)) # False
    print(isinstance(b'str',bytes)) # True

    # print(b'127.0.0.1'.split('.')) # Error
    print(b'127.0.0.1'.split(b'.'))

    segments = b'127.0.0.1'.split(b'.')

    print(all(segment in VALID_IPv4_SEGMENTS for segment in segments))
