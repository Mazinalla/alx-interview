#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row of Pascal's Triangle
    
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Sum of two elements from the previous row
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    return triangle
