#!/usr/bin/python3
"""Rotate matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a matrix in place by 90 deg"""
    length = len(matrix)
    for i in range(length):
        matrix[i].reverse()

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()
    for i in range(length):
        matrix[i].reverse()
