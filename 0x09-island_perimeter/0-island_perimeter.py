#!/usr/bin/python3
'''Island perimeter module'''


def island_perimeter(grid):
    '''Island perimeter function'''
    if not grid:
        return 0
    row = len(grid)
    column = len(grid[0])
    perimeter = 0

    for i in range(row):
        for j in range(column):
            square = 4
            if grid[i][j]:
                try:
                    if j < column - 1 and grid[i][j + 1]:
                        square -= 1
                    if j > 0 and grid[i][j - 1]:
                        square -= 1
                    if i < row - 1 and grid[i + 1][j]:
                        square -= 1
                    if i > 0 and grid[i - 1][j]:
                        square -= 1
                except IndexError:
                    pass
                perimeter += square
    return perimeter
