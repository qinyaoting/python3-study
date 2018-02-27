#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from multiprocessing import Process, Pool, Queue
import os, time, random

__author__ = 'chin'

def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def write(q):
    print("Process to write:%s" % os.getpid())
    for value in ['A','B', 'C', 'D']:
        q.put(value)
        time.sleep(random.random())

def read(q):
    print("Process to write:%s" % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


# 多线程

if __name__ == '__main__':
    # print('Process start at %s' % os.getpid())
    # # 注意调用fork(), 会返回两次
    # pid = os.fork()
    #
    # if pid == 0:
    #     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    # else:
    #     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


    # 启动一个子线程
    # print('parent process %s' % os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # print('child process will start')
    # p.start()
    # p.join()
    # print('child process end')


    # 用进程池启动多个子线程
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


    import subprocess

    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('exit code:', r)

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

    #
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
