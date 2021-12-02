import matplotlib.pyplot as plt
import scipy.interpolate import UnivariateSpline
from numpy import *
x = [0.2, 0.6, 1.1, 1.8, 2.6]
y = [3.34, 4.53, 2.75, 3.91, 3.57]
spl = UnivariateSpline (x,y)
xs = linspace(0, 4.5, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()