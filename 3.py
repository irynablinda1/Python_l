import math;
def equation(x):
    return x**4+4*x**3-8*x**2-17
def fequation(x):
    return 4*x**3+12*x**2-16
def ffequation(x):
    return 12*x**2+24*x


def newton(a, b, e):
    if(equation(a)*ffequation(a) > 0):
        x = b
    else: 
        x = a
        
    h = equation(x)/fequation(x)
    x = x-h
    
    while(abs(h)<=e)
        return x
        return equation(x)
    else:
        h = equation(x) / fequation(x)
        x = x - h
        
print(newton(-5, -4, 0.0001))