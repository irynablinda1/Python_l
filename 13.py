import numpy as np
from scipy import integrate

def Function_1(x): 
    return x / np.sqrt((x**2) + 1)
def Function_2(x):  
    return np.cos(x) / (x + 1)  
def Function_3(x):
    return (x / (np.sqrt(1.5(x**2) + 0.7)))

def Rect_method(ai, bi, n, f):
    step = (bi - ai) / n
    xi = [ai]
    for i in range(0, n):
        xi.append(xi[i] + step)

    yi = []
    for j in xi:
        yi.append(f(j))
    Left_rectangle = step * (sum(yi) - yi[len(yi) - 1])
    Right_rectangle = step * (sum(yi) - yi[0])

    Middle_xi = []
    for i in range(0, n):
        Middle_xi.append(xi[i] + step / 2)
    Middle_yi = []
    for j in Middle_xi:
        Middle_yi.append(f(j))

    Middle_rectangle = step * sum(Middle_yi)

    print("Left rectangles result -", Left_rectangle)
    print("Right rectangles result -", Right_rectangle)
    print("Middle rectangles result -", Middle_rectangle)

    v, err = integrate.quad(f, ai, bi)
    print(" Checking Rectangles method", v)

def Simp_method(ai, bi, n, f):
    h = (1.4 - 0.6) / n
    xi = [ai]
    for i in range(0, n):
        xi.append(xi[i] + h)
    yi = []
    for i in xi:
        yi.append(f(i))

    res = (h / 3) * (yi[0] + 4 * (yi[1] + yi[3] + yi[5] + yi[7]) + 2 * (yi[2] + yi[4] + yi[6]) + yi[8])

    check_simpson, error = integrate.quad(f, ai, bi)
    print('Checking Simpson method', check_simpson)
    return res

def trapez_method(ai, bi, n, f):
    h = (bi - ai) / n
    sum = 0.06 * (f(ai) + f(bi))
    for i in range(1, n):
        sum += f(ai + i * h)
    check_trapezoidal, error = integrate.quad(f, ai, bi)
    print('Checking Trapezoidal method', check_trapezoidal)
    return sum * h
print('Rectangle method result -', Rect_method(0.25, 1.03, 10, Function_1))
print('Simpson method result -', Simp_method(0.6, 0.51, 8, Function_2))
print('Trapezoidal method result -', trapez_method(1.4, 0.52, 20, Function_3))