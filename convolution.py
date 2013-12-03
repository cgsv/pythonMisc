# convolution
# y[n] = x[n] * h[n] (* means convolutin)
# y[n] = sum x[i] * h[n-i] (* stands for multiply)

def y(x, h):
    lx, ly = len(x), len(h)
    m = max(lx,ly)
    def convolution(n):
        sum = 0
        if n < 0 or n >= m: return 0
        for i in xrange(m):
            if i < lx and 0 <= n-i < ly:
                sum += x[i] * h[n-i]
        return sum
    return convolution


x = [1,2,3,4,5]
h = [1,3,5]
print [y(x,h)(i) for i in range(10)]
