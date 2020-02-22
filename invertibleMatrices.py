import numpy as np
import pickle
import time

'''an algorithm that finds all invertible 4x4 matrices. 
There are 3^16 possible matrices, which is about 43 million.
Of those matrices, only some are invertible. This algorithm
counts to 3^16 in ternary, and reads each value into a matrix.
It then takes the determinant of that matrix to determine if
the matrix is invertible. If invertible, the matrix is added
to the list 'matrices,' which stores all invertible matrices.
'''

# BUGS: currently giving some nonzero determinants due to a float rounding error.
# Also, it may be better to integrate this code into verifier and find invertible matrices and use
# them as we go, since this outputs a 3.5 Gb file, and it takes longer to load the file in
# Verifier than it does to run the search.

# CURRENTLY ONLY FINDING 2x2 MATRICES

matrices = []
curr = time.time()
for i in range(3**16):
    values = np.base_repr(i, 3)  # i in base 3
    matrix = np.zeros((4, 4))
    for j in range(3, -1, -1):  # read all entries of values into matrix
        for k in range(3, -1, -1):
            entry = int(values[len(values)-1])
            matrix[j, k] = entry
            values = values[0:len(values)-1]
            if values == '':
                break
        if values == '':
            break
        matrix = matrix.astype(int)
    if np.mod(np.linalg.det(matrix), 3).astype(int) != 0:  # if matrix has nonzero
                                        # determinant, add to matrices
        matrices.append(matrix)

print(time.time()-curr)

np.save('matrices.npy', matrices)
