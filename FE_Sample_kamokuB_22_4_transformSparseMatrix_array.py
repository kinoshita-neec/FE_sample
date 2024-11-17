# FEサンプル問題'22公開　問4 疎行列

def transformSparseMatrix(matrix:list):
    sparseMatrix = [[],[],[]]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] != 0:
                sparseMatrix[0].append(i)
                sparseMatrix[1].append(j)
                sparseMatrix[2].append(matrix[i][j])
    
    return sparseMatrix

matrix = [[3,0,0,0,0],
          [0,2,2,0,0],
          [0,0,0,1,3],
          [0,0,0,2,0],
          [0,0,0,0,1]]

newMatrix = transformSparseMatrix(matrix)

print("",newMatrix[0],"\n",newMatrix[1],"\n",newMatrix[2])