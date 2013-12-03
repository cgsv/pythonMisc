import socket, sys, time, random

address = ('localhost', 1060)
s = socket.socket()

if sys.argv[1] == 'server':
    cs = []
    s.bind(address)
    s.listen(2)
    num = 0

    while True:
        ss, addr = s.accept()
        cs.append(ss)
        if len(cs) >= 2:
            break

    while True:
        a = random.randint(0,100)
        b = random.randint(0,100)
        cs[0].send('You get ' + repr(a))
        cs[1].send('You get ' + repr(b))
        
        ma = cs[0].recv(200)
        mb = cs[1].recv(200)

        if ma == mb:
            cs[0].send('Equal')
            cs[1].send('Equal')
        else:
            cs[0].send('Not Equal')
            cs[1].send('Not Equal')



if sys.argv[1] == 'client':
    s.connect(address)
    while True:
        data = s.recv(200)
        print data
        ans = raw_input('Your answer: ')
        s.send(ans)
        data = s.recv(200)
        print data
    s.close()

