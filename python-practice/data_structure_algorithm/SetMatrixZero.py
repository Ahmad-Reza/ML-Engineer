# Problem - Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# 1. Brute force technique.
def setZeroes(matrix: list[list[int]]) -> None :
    
    # find the zeroes and update their entire row and column 0 in the matrix.
    for rowIndex, row in enumerate(matrix):
        for colIndex, element in enumerate(row):
                if element == 0:
                    markRowColumnForZero(rowIndex, colIndex, matrix)
                    
    # change the -1 value with 0
    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[rowIndex])):
            if matrix[rowIndex][colIndex] == -1:
                matrix[rowIndex][colIndex] = 0
                
    print(matrix)
                
def markRowColumnForZero(rowIndex: int, colIndex: int,  matrix: list[list[int]]) -> None:
    for index, element in enumerate(matrix[rowIndex]):
        if element != 0:
            matrix[rowIndex][index] = -1
    
    for index, element in enumerate(matrix):
        if element[index] != 0:
           matrix[index][colIndex] = -1
                
            
matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

setZeroes(matrix)