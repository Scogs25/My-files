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
        row_list=[]
        for j in range(len(matrixA[0])):
            m_new_ij=matrixA[i][j]+matrixB[i][j]
            row_list.append(m_new_ij)
        matrixSum.append(row_list)
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
def get_row(matrix, row):
    return matrix[row]
def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
            wanted=matrix[i][column_number]
            column.append(wanted)
    return column

def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
print(dot_product([6],[7])) 
def matrix_multiplication(matrixA, matrixB):
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    result = []
    for r in range(m_rows):
        row_result = []
        rowA = get_row(matrixA, r)
        for c in range(p_columns):
            colB = get_column(matrixB, c)
            dot_prod = dot_product(rowA, colB)
            row_result.append(dot_prod)
        result.append(row_result)
    return result
print(matrix_multiplication(A,B))
def transpose(matrix):
    matrix_transpose = []
    for c in range(len(matrix[0])):
        new_row = []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        matrix_transpose.append(new_row)
    return matrix_transpose
def matrix_multiplication(matrixA, matrixB):
    product = []
    transposeB = transpose(matrixB)
    for r1 in range(len(matrixA)):
        new_row = []
        for r2 in range(len(transposeB)):
            dp = dot_product(matrixA[r1], transposeB[r2])
            new_row.append(dp)
        product.append(new_row)
    return product
def identity_matrix(n):
    identity = []
    for r in range(n):
        new_row = []
        for c in range(n):
            if r == c: # Diagonals are only ones
                new_row.append(1)
            else: # Everything else is zero
                new_row.append(0)
        identity.append(new_row)
    return identity
def inverse_matrix(matrix):
    inverse = []
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')
    if len(matrix) > 2:
        raise NotImplementedError('this functionality is not implemented') 
    if len(matrix) == 1:
        inverse.append([1 / matrix[0][0]])
    elif len(matrix) == 2:
        if matrix[0][0] * matrix[1][1] == matrix[0][1] * matrix[1][0]:
            raise ValueError('The matrix is not invertible.')
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            
            factor = 1 / (a * d - b * c)
            inverse = [[d, -b],[-c, a]]
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = factor * inverse[i][j]
    return inverse
G=[[2,2],
[5,4]]
F=[5,3]
print(np.linalg.det(G))
print(np.linalg.solve(G,F))
print(np.linalg.inv(G))
eig_val,eig_vec=np.linalg.eig(G)
print(eig_val)
print(eig_vec)
