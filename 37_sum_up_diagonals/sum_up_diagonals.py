def sum_up_diagonals(matrix):
    """Accepts a matrix as input. Initializes an output to zero, goes through the matrix
    and adds up the integers in the spatial diagonals of the matrix.
    Does this by starting with a count at 0 and a matrix_size one less than the matrix length
    (to represent the proper index number). Iterates through each list in the matrix (or each row)
    and adds the ints at index count and index matrix_size. In the first list, this will be the 1st number
    and last number (one from each diagonal); in the second list, this will be the 2nd number and 2nd to last number
    (again, one from each diagonal).
    """
    output = 0
    count = 0
    matrix_size = len(matrix) - 1
    for lst in matrix:
        output = output + lst[count] + lst[matrix_size]
        matrix_size -= 1
        count += 1
    return output