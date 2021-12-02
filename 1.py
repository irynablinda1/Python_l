# 1.2 завдання (різниця матриць)
import numpy as np
  
A = np.array([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
  
B = np.array([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
  
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
  
print("Subtraction of two matrix")
print(np.subtract(A, B))