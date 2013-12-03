def stream(i):
    n = i
    while True:
        yield n
        n += i

def merge(sa, sb):
    a, b = sa.next(), sb.next()
    while True:
        if a < b:
            yield a
            a = sa.next()
        elif a > b:
            yield b
            b = sb.next()
        else:
            yield a
            a, b = sa.next(), sb.next()

def merges(*streams):
    if len(streams) == 1: return streams[0]
    return merge(streams[0],merges(*streams[1:]))

def printn(stream, n):
    for i in xrange(n):
        print stream.next(),
    print

if __name__ == '__main__':
    #printn(merge(stream(5),merge(stream(2),stream(3))), 100)
    printn(merges(stream(2), stream(3), stream(5)), 100)

