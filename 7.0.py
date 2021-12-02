import matplotlib.pyplot as plt
import numpy as np
from numpy import *

#Example 10
t = linspace(-1, 9, 17) 
y1 = -5*cos(10*t)*sin(3*t)/(t**(1/2)) 
fig, ax = plt.subplots()
ax.plot(t, y1)
ax.grid()
plt.plot(t, y1, 'g-')
plt.xlabel('t') 
plt.ylabel('y') 
plt.title('Variant11') 
plt.legend(['-5*cos(10*t)*sin(3*t)/(t**2)'], # список легенди  
           loc='upper left') # положення легенди 
plt.show()

#Example 11
t = linspace(-1, 3, 17) 
y1 = -5*cos(10*t)*sin(3*t)/(t**2) 
fig, ax = plt.subplots()
ax.plot(t, y1)
ax.grid()
plt.plot(t, y1, 'g-')
plt.xlabel('t') 
plt.ylabel('y') 
plt.title('Variant11') 
plt.legend(['-5*cos(10*t)*sin(3*t)/(t**2)'], # список легенди  
           loc='upper left') # положення легенди 
plt.show()




#Example 12
t = linspace(0, 3, 15) 
y1 = 5*sin(10*t)*sin(3*t)/(t**2) 
fig, ax = plt.subplots()
ax.plot(t, y1)
ax.grid()
plt.plot(t, y1, 'g-')
plt.xlabel('t') 
plt.ylabel('y') 
plt.title('Variant12') 
plt.legend(['5*sin(10*t)*sin(3*t)/(t**2)'], # список легенди  
           loc='upper left') # положення легенди 
plt.show()



