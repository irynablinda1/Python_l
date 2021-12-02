import matplotlib.pyplot as plt
from numpy as np

def taylor(x):
  a = 0
  f = a**2*(np.sin(2*a))
  ff = 2*a*(2*np.cos(2*a))
  fff = 2*(-4 * np.sin(2*a))
  ffff = -8*np.cos(2*a)
  y = f + ff*x + fff*(x**2/2) + ffff*(x**3/6)
  
  return y

x = np.linspace(-2,2)
f = x**2*(np.sin(2*x))
y_taylor = taylor(x)
plt.plot(x, f, 'g', x, y_taylor, 'r')
plt.title('dftg')
plt.legend(['fgh', 'fgh'])
plt.grid()
plt.show()