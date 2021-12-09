import numpy as np

a_2d = [[11,12,13],[21,22,23],[31,32,33]]

A_2d = np.array(a_2d)

A = np.array([[0,1,1],[1,0,1]])
B = np.array([[1,1],[1,1],[-1,1]])

# Dot Product
C = np.dot(A,B)
print(C)