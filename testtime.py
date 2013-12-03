import time

def timeit(func):
    def __fun(*args):
        tstart = time.clock()
        res = func(*args)
        tend = time.clock()
        print "Total time:", tend - tstart
        return res
    return __fun

@timeit
def getsum(n):
    sum = 0
    for i in range(n):
        sum += (i + 1)
    return sum

print getsum(20000)
print getsum(200000)
