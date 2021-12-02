import matplotlib.pyplotplot as plt
import nympy as np

x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
y = np.array([0.84, 0.84, 0.83, 0.82, 0.8, 0.77, 0.73, 0.7, 0.78, 0.77])

x1 = sum(x)/10
x2 = sum(x**2)/10
y1 = sum(y)/10
yx = sum(x*y)/10

a1 = (yx - x1*y1)/(x2 - x1**2)
a0 = y1 - a1 * x1

x_graph = np.array([-6,6])
y_graph = np.array(a0 + a1*x_graph)

plt.plot(x_graph, y_graph)
plt.title("Variant 4")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
