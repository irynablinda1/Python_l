import numpy as np
from math import factorial

x = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637]
h = x[1] - x[0]
x = 0.1
q = (x - 0.)/h
k = 0
def n(y,j):
    mas = []
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j -= 1
        return n(mas, j)

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print (n_1)
