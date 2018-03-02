#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
import logging
from multiprocessing import Process, Pool, Queue
import os, time, random
from sys import stdout

__author__ = 'chin'

class ColourFormatter(logging.Formatter):

    def format(self, record):
        s = super(ColourFormatter, self).format(record)
        if record.levelno == logging.CRITICAL:
            return "\x1b[31;1m%s\x1b[0m" % s  # bright red
        elif record.levelno == logging.ERROR:
            return "\x1b[33;1m%s\x1b[0m" % s  # bright yellow
        elif record.levelno == logging.WARNING:
            return "\x1b[33m%s\x1b[0m" % s    # yellow
        elif record.levelno == logging.INFO:
            return "\x1b[36m%s\x1b[0m" % s    # cyan
        elif record.levelno == logging.DEBUG:
            return "\x1b[34m%s\x1b[0m" % s    # blue
        else:
            return s

class Watcher(object):

    handlers = {}

    def __init__(self, logger_name):
        # ???
        super(Watcher, self).__init__()
        # 构造方法需要传入一个名称
        self.logger_name = logger_name
        # 用名称构造logger
        self.logger = logging.getLogger(self.logger_name)
        # 构造formatter
        self.formatter = ColourFormatter.format("%(asctime)s  %(message)s", "111")

    # ???
    def __enter__(self):
        self.watch()
        return self

    # ???
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def watch(self, level=logging.INFO, out=stdout):
        # 清除字典中的数据
        self.stop()
        # 由stdout构造handler
        handler = logging.StreamHandler(out)
        # 给handler设置formatter
        handler.setFormatter(self.formatter)
        # handler加入字典中
        self.handlers[self.logger_name] = handler
        # logger添加handler
        self.logger.addHandler(handler)
        # logger设置level
        self.logger.setLevel(level)

    def stop(self):
        try:
            self.logger.removeHandler(self.handlers[self.logger_name])
        except KeyError:
            pass

if __name__ == '__main__':

    # python 惯用写法004
    #
    flag = True
    level = 'info' if flag else 'debug'

    level = 'info'
    if not flag:
        level = 'debug'

    # 写在一行, 比较简练

    # Watcher('neo4j').watch(logging.INFO, stdout)

    # python惯用写法 005
    # 用分隔符将字符串划分为三部分
    paramters = {'lucky':'girl', 'jack':'boy'}
    name, _, value = 'lucy=girl'.partition('=')
    print('%s %s %s' % (name, _, value))
    if value == "" and name in paramters:
        del paramters[name]
    else:
        paramters[name] = value
