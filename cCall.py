class cCall:
    def __init__(self):
        self.count = 0

    def decoCall(self, fun):
        def g(*x):
            self.count += 1
            print "called", self.count, "times. args=", x
            return fun(*x)
        return g

    def resetCount(self):
        self.count = 0


class memDec:
    def __init__(self, maxlen):
        self.memdict = {}
        self.max = maxlen
        
    def memfun(self, fun):
        def g(x):
            if self.memdict.has_key(x): return self.memdict[x]
            res = fun(x)
            self.memdict[x] = res
            while len(self.memdict) > self.max:
                self.memdict.popitem()
            return res
        return g
    
