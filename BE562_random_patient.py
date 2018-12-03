import numpy
import numpy as np

import random

for k in range(1, 101):

    #set the range of the list (make it possible for repetitive num)
    num_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4]

    #initialize the matrix
    matrix = np.zeros((90, 12))
    #colums = {chrom1, chrom2, chrom3, gene1, gene2, gene3, gene4, gene5, gene6, gene7, gene8, cellnum}

    for i in range(90):
        for j in range(12):
            matrix[i][j] = random.choice(num_list)

    print(matrix)
        
    np.savetxt('patient' + str(k) + '_DCID.txt', matrix.astype(int), fmt='%s')
