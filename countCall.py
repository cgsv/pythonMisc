import sys

def countCall(fun):
    count = [0]
    def g(*x):
        count[0] += 1
        res = fun(*x)
        print "called", count[0], "times. res =", res
        return res
    return g

def countCall2():
    count = [0]
    def ff(mode):
        def setcount(n): count[0] = n
        def getcount(): return count[0]
        def g(fun):
            def fg(*x):
                count[0] += 1
                print "called", count[0], "times."
                return fun(*x)
            return fg
        if mode == 0: return g
        if mode == 1: return getcount
        if mode == 2: return setcount
    return ff

cc = countCall2()
@cc(0)
        

@countCall
def fab(n):
    if n == 0 or n == 1: return 1
    return fab(n-1) + fab(n-2)

if __name__ == '__main__':
    n = int(sys.argv[1])
    res = fab(n)
    print "fab("+str(n)+ ")=", res
