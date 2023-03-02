import numpy as np


A = np.array([[-1, 3], [3, 2]], dtype=np.dtype(float))
b = np.array([7, 1], dtype=np.dtype(float))

# reshape first parmeter is the row number and second is column
# hstack add another matrix horizontally
A_system = np.hstack((A, b.reshape((2,1))))

print(A_system[1])
# print(b.reshape((2,1)))
#solution 
x = np.linalg.solve(A, b)

#finding the determinant
d = np.linalg.det(A)

# print(f'The value of A: \n {A}')
# print(f'The value of b: \n {b}')
# print(f'The shape of A: \n {A.shape}')
# print(f'The shape of b: \n {b.shape}')
# print(f'The solution: \n {x}')
# print(f'The Determinant: \n {d: .2f}')

