#!/usr/bin/python3
"""
Contains pascal's Triangle fiunction
"""

def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(1, n+1):
            row = []
            for j in range(i):
                if j == 0 or j == i-1:
                    n = 1
                    row.append(n)
                else:
                    n = triangle[i-2][j-1] + triangle[i-2][j]
                    row.append(n)
            triangle.append(row)

        return triangle
