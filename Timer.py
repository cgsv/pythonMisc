import time
from math import sqrt
from matMul import fabimul, fibonacci

class Timer:

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def fabi(n):
    if n == 0 or n == 1: return 1
    return fabi(n-1) + fabi(n-2)

def fabi2(n, a = 1, b = 1):
    if n == 0: return a
    return fabi2(n-1, b, a+b)

def fabi3(n):
    a, b = 1, 1
    for i in range(n):
        a , b = b, a + b
    return a

def fibb():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def fibgen(n):
    a = sqrt(5)
    b = (1 + a)/2
    c = (1 - a)/2
    return (b**n - c**n)/a


def test(fun, n):
    with Timer() as t:
#        for i in range(n):
#            print fun(i),
        fun(n)
        print
    print fun.__name__, t.interval

def test1(fun, n):
    with Timer() as t:
        for i in range(n):
            fun(i),
#        fun(n)
        print
    print fun.__name__, t.interval

if __name__ == '__main__':
    n = 50000
#    test(fabi, 30)
#    test(fabi2, n)
    test(fabi3, n)
    ite = fibb()
    itefun = lambda x: ite.next()
    test1(itefun, n)
    test(fabimul, n)
    test(fibonacci, n)

