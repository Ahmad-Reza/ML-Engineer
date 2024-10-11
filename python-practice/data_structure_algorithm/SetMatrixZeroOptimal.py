# Problem - Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
def set_zeroes(matrix: list[list[int]], row_size: int, column_size: int) -> None:
    first_col_zero = False  # Using a boolean for readability
    
    # Step 1: Mark rows and columns that need to be zeroed
    for i in range(row_size):
        if matrix[i][0] == 0:
            first_col_zero = True
        for j in range(1, column_size):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row
                matrix[0][j] = 0  # Mark the column
    
    # Step 2: Use marks to set elements to zero
    for i in range(1, row_size):
        for j in range(1, column_size):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Step 3: Zero the first row if necessary
    if matrix[0][0] == 0:
        for j in range(column_size):
            matrix[0][j] = 0

    # Step 4: Zero the first column if necessary
    if first_col_zero:
        for i in range(row_size):
            matrix[i][0] = 0

# Sample matrix to test the function
matrix = [
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1]
]

# Apply the function and print the result
set_zeroes(matrix, len(matrix), len(matrix[0]))
print(matrix)
