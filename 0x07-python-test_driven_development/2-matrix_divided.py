#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
        This function divides each member of "matrix" by "div"
        and returns a new matrix of the same order as "matrix"
        whose elements are the quotients of that division.
    """
    if not(
            isinstance(matrix, list) and
            all(isinstance(row, list) and all(isinstance(element, (int, float))
                for element in row) for row in matrix)
    ):
        raise TypeError('matrix must be a matrix
                        (list of lists) of integers/floats')

    if not (len(set(len(row) for row in matrix)) == 1):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
