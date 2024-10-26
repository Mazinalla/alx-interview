#!/usr/bin/python3

"""
This module contains the function pascal_triangle(n),
which returns a list of lists of integers representing Pascal's triangle of n.
"""


def pascal_triangle(n):

    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """

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
