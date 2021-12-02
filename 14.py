import matplotlib.pyplot as plt 
from numpy import * 
from math import * 
 
def metodeuler(x, y): 
    return x + math.cos(y/sqrt(7)) 
 
def metodeuler_coshi(x, y): 
    return x + math.cos(y/3,14) 
 
def method1(metodeuler, x, y): 
    h = 0.2 
    x = 0.5 
    y = 1.5 
    xarr = ([]) 
    yarr = ([]) 
    for i in range (0, 10): 
        x += h 
        xarr.append([x]) 
        y += h* metodeuler(x, y) 
        yarr.append([y]) 
    plt.plot(xarr, yarr) 
    plt.title("Variant 4 - ") 
    plt.xlabel('х') 
    plt.ylabel('y') 
    plt.grid() 
    plt.show() 
    return xarr, yarr 
 
def method2(metodeuler_coshi, x, y): 
    h = 0.2 
    x = 1.7 
    y = 2.7 
    xarr = ([]) 
    yarr = ([]) 
    for i in range (0, 10): 
        x += h 
        xarr.append([x]) 
        
        y += h/2 * (metodeuler_coshi(x, y) + metodeuler_coshi(x+h, metodeuler_coshi(x, y))) 
        yarr.append([y]) 
    plt.plot(xarr, yarr) 
    plt.title("Variant 4 -") 
    plt.xlabel('х') 
    plt.ylabel('y') 
    plt.grid() 
    plt.show() 
    return xarr, yarr 
 
print(method1(metodeuler, 0.5, 1.5)) 
print(method2(metodeuler_coshi, 1.7, 2.7))