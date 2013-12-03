def mulMat(ma, mb):
    arow,acol = len(ma),len(ma[0])
    brow,bcol = len(mb),len(mb[0])
    if acol != brow: return
    return [[reduce(lambda x,y: x+y, \
                        map(lambda x,y: x*y, ma[i],[m[j] for m in mb])) \
                 for j in range(bcol)] for i in range(arow)]

def expMat(ma, n):
    if n == 1: return ma
    return mulMat(ma, expMat(ma, n - 1))

def expMat2(ma, n):
    if n == 0: return
    if n == 1: return ma
    if n % 2 == 0:
        tma = expMat2(ma, n/2)
        return mulMat(tma, tma)
    return mulMat(ma, expMat2(ma, n - 1))

def fabimul(n):
    fiba = [[0, 1], [1, 1]]
    return expMat2(fiba, n + 1)[1][0]

def fibonacci(n):
    def iter(a, b, p, q, n):
        if n == 0:
            return b
        elif n % 2 == 0:
            return iter(a, b, p * p + q * q, 2 * p * q + q * q, n / 2)
        else:
            return iter(a * (p + q) + b * q, a * q + b * p, p, q, n - 1)
    return iter(1, 0, 0, 1, n)
