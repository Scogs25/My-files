import numpy as np
import numpy.linalg
c=np.array([[3,-3],[3,-2]])
d=np.array([-9,4])
print(numpy.linalg.solve(c,d))
m = [
    [8, 7, 1, 2, 3],
    [1, 5, 2, 9, 0],
    [8, 2, 2, 4, 1]
]
r = []
for i in range(len(m)):
    row = m[i]
    new_row = [] 
    for j in range(len(row)):
        m_ij = 5*m[i][j]
        new_row.append(m_ij)
    r.append(new_row)
print(r)
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m_ij = matrix[i][j]
            print(m_ij, '\t', end="")
        print('\n') # prints a new line
    return
print(matrix_print(m))
def matrix_addition(matrixA, matrixB):
    matrixSum = []
    row_list = []
    for i in range(len(matrixA)):
        row=matrixA[i]
        for j in range(len(row)):
            m_new_ij=matrixA[i][j]+matrixB[i][j]
            row_list.append(m_new_ij)
        matrixSum.append(row_list)
        row_list=[]
    return matrixSum
A = [
    [2,5,1], 
    [6,9,7.4], 
    [2,1,1], 
    [8,5,3], 
    [2,1,6], 
    [5,3,1]
]
B = [
    [7, 19, 5.1], 
    [6.5,9.2,7.4], 
    [2.8,1.5,12], 
    [8,5,3], 
    [2,1,6], 
    [2,33,1]
]
print(matrix_addition(A, B))