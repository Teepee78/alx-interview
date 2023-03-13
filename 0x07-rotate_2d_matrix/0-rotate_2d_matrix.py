#!/usr/bin/python3


# Make first array
def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix in place"""

    length_array = len(matrix)
    # array to remove values from
    array_index = -1
    # position to insert in all arrays
    position = 0
    # index of arrays
    j = 0

    for i in range(length_array):
        # position to remove
        k = i
        length = len(matrix[array_index])
        array = matrix[array_index]
        while k < length and array != [] and j < length_array:
            num = array[k]

            matrix[j].insert(position, num)
            array.pop(k)

            if matrix[j] == array:
                k += 1
            j += 1
        k += 1
        position += 1
        array_index -= 1
        j = 0
