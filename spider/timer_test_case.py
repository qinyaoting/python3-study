import threading


def giveup_parse():
    print('=======None')
    # return None
    raise ZeroDivisionError('000000000000')

def run():

    print('running........')
    # timer = threading.Timer(2.0, giveup_parse()) mbd
    timer = threading.Timer(2.0, giveup_parse)
    timer.start()
    print('timer..........')


if __name__ == '__main__':
    run()