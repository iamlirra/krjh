import multiprocessing
from random import randint
from time import time
import array


def f():
    ar = [randint(0, 10) for i in range(10 ** 9)]
    if sum(ar) % 2 == 0:
        return True
    else:
        return False


th1 = multiprocessing.Process(target=f)
th2 = multiprocessing.Process(target=f)
th3 = multiprocessing.Process(target=f)
th4 = multiprocessing.Process(target=f)
processes = [th1, th2, th3, th4]


if __name__ == '__main__':
    start = time()
    f()
    f()
    f()
    f()
    end = time()
    print('4 раза последовательно:', end - start)
    start = time()
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    for i in processes:
        i.join()
    end = time()
    print('По 1 разу в 4 процессах:', end - start)
