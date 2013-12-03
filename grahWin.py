from graphics import *
import math
import random
import pdb

def smooth(fun):
    def g(x):
        dx = 1
        return (fun(x) + fun(x-dx) + fun(x+dx))/3.0
    return g

def mainwin(funlist, funlist2):
    win = GraphWin("Plot", 800, 400)
    win.setCoords(-5, -5, 105, 105)
    drawFun(funlist, win, 'black')
    drawFun(funlist2, win, 'red')
    win.getMouse()
    win.close()

def drawFun(funlist, wind, color):
    length = len(funlist)
    for i in range(1,length):
        p1 = Point(funlist[i-1][0], funlist[i-1][1])
        p2 = Point(funlist[i][0], funlist[i][1])
        li = Line(p1, p2)
        li.setFill(color)
        li.draw(wind)    

def scalelist(li, a, b):
    ma, mi = max(li), min(li)
    k = (b - a) / (ma - mi)
    return map(lambda x:a+(x-mi)*k, li)

def getFunlist(fun, a, b, s = 0, autoscale = True):
    xlist, ylist = [], []
    if s == 0: s = (b - a) / 100.0
    s = float(s)
    m = a
    while m <= b:
        xlist.append(m)
        ylist.append(fun(m))
        m += s
    if autoscale:
        xlist = scalelist(xlist,0,100.0)
        ylist = scalelist(ylist,0,100.0)
    return zip(xlist,ylist)

if __name__ == '__main__':
#    pdb.set_trace()
    mainwin(getFunlist(smooth(lambda x: x * x), 0, 10, 0, False), \
            getFunlist(lambda x: x * x, 0, 10, 0, False))
