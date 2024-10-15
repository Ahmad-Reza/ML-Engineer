# Program to generate Pascal's Triangle
# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

def generate_pascal_triangle(n: int)-> list[list[int]]:
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        
        row.append(1)
        triangle.append(row)
            
    return triangle      


rows = 5
pascal_triangle = generate_pascal_triangle(rows)



print(f'Pascal triangle - ')
for row in pascal_triangle:
    print(row)

    