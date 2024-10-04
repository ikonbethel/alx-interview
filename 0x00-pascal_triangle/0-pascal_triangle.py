#!/usr/bin/python3
'''Pascal Triangle'''


def pascal_triangle(n):
    '''Pascal triangle'''
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1], [1, 1]]
    if n == 2:
        return triangle
    for i in range(2, n):
        last = triangle[i - 1]
        current = []
        for j in range(0, len(last) + 1):
            a = last[j - 1] if j - 1 >= 0 else 0
            b = last[j] if j < len(last) else 0
            current.append(a + b)
        triangle.append(current)
    return triangle
