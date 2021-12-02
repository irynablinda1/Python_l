#прямий хід
import numpy as np
import sys

n = int(input('Enter number of unknowns: '))

a = np.zeros((n,n+1))
x = np.zeros(n)


print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))


for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]


x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]


print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')


#зворотній хід
import numpy as np
import sys

n = int(input('Enter order of matrix: '))

a = np.zeros((n,2*n))

print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(n):        
    for j in range(n):
        if i == j:
            a[i][j+n] = 1

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(2*n):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(n):
    divisor = a[i][i]
    for j in range(2*n):
        a[i][j] = a[i][j]/divisor

print('\nINVERSE MATRIX IS:')
for i in range(n):
    for j in range(n, 2*n):
        print(a[i][j], end='\t')
    print()