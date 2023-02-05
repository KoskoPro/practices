import numpy as np


def validate_sudoku(board):
    '''
    Sudoku board validator
    #1. Sum of all columns equal 45, no repeating digits  ==> out list(bool)
    #2. Sum of all rows equal 45, no repeating digits ==> out list(bool)
    #3. Split into 3x3 matrices (boxes), sum of digits equal 45, no repeating digits ==> out list(bool)
    :param board: array 9x9
    :return: bool
    '''
    arr = np.array(board)

    column = all([sum(set(el)) == 45 for el in arr])
    row = all([sum(set(arr[:, el])) == 45 for el in range(9)])

    x_row = 0
    boxes = []

    while x_row < 9:
        y_column = 0
        while y_column < 9:
            matrix = arr[x_row:x_row + 3, y_column:y_column + 3]
            boxes.append(sum(set([name for group in matrix for name in group])) == 45)
            y_column += 3
        x_row += 3

    return column and row and all(boxes)


validate = [[8, 4, 7, 2, 6, 5, 1, 9, 3],
            [1, 3, 6, 7, 9, 8, 2, 4, 5],
            [9, 5, 2, 1, 4, 3, 8, 6, 7],
            [4, 2, 9, 6, 7, 1, 5, 3, 8],
            [6, 7, 8, 5, 3, 2, 9, 1, 4],
            [3, 1, 5, 4, 8, 9, 7, 2, 6],
            [5, 6, 4, 9, 1, 7, 3, 8, 2],
            [7, 8, 1, 3, 2, 4, 6, 5, 9],
            [2, 9, 3, 8, 5, 6, 4, 7, 1]]
print(validate_sudoku(validate))
