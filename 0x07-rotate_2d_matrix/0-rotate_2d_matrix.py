#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Prototype: def rotate_2d_matrix(matrix):
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix to 90 degrees clockwise.
    """
    w = len(matrix[0])
    h = len(matrix)
    i = h - 1
    j = 0
    rotated_mat = []
    row_mat = []

    while j < w:
        row_mat.append(matrix[i][j])
        if i == 0:
            rotated_mat.append(row_mat)
            j += 1
            i = h
            row_mat = []
        i -= 1

    for i, j in enumerate(rotated_mat):
        matrix[i] = rotated_mat[i]
