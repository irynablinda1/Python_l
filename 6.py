import math
from scipy import optimize

x0 = 1.2
y0 = 1.1

def f1(y):
    return 1,5 - math.cos(x)

def f2(x):
    return 1 + math.sin(y-0.5)/2

def iteration (x,y):
    n = 1
    e = 0.001

    xn = x
    yn = y

    xn1 = f2(x)
    yn1 = f1(y)

    while ((abs(yn1-yn) >= e) & (abs(xn1-xn) >= e)):
        yn = yn1
        xn = xn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n = n + 1

    print ("y = ", xn, "x = ", yn)