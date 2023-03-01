#!/usr/bin/python3
"""N queens algorithm"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def diagonal(result: list, x: int, y: int):
    """
    Checks if a cell is unattacked

    Args:
        result (list): List of cells that can attack queen
        x (int): Queens's x coordinate
        y (int): Queen's y coordinate

    Returns:
        bool: True if the cells is unattacked, False otherwise
    """

    # Check left downwards
    temp_x = x
    temp_y = y
    while temp_x > 0 and temp_y > 0:
        temp_x -= 1
        temp_y -= 1
        if [temp_x, temp_y] in result:
            return False

    # Check right upwards
    temp_x = x
    temp_y = y
    while temp_x < N and temp_y < N:
        temp_x += 1
        temp_y += 1
        if [temp_x, temp_y] in result:
            return False

    # Check right downwards
    temp_x = x
    temp_y = y
    while temp_x < N and temp_y > 0:
        temp_x += 1
        temp_y -= 1
        if [temp_x, temp_y] in result:
            return False

    # Check left upwards
    temp_x = x
    temp_y = y
    while temp_x > 0 and temp_y < N:
        temp_x -= 1
        temp_y += 1
        if [temp_x, temp_y] in result:
            return False

    return True


def vertical(result: list, x: int, y: int):
    """
    Checks if a cell is unattacked

    Args:
        result (list): List of cells that can attack queen
        x (int): Queens's x coordinate
        y (int): Queen's y coordinate

    Returns:
        bool: True if the cells is unattacked, False otherwise
    """

    # Check left
    temp_x = x
    while temp_x > 0:
        temp_x -= 1
        if [temp_x, y] in result:
            return False

    # Check right
    temp_x = x
    while temp_x < N:
        temp_x += 1
        if [temp_x, y] in result:
            return False

    # Check downwards
    temp_y = y
    while temp_y > 0:
        temp_y -= 1
        if [x, temp_y] in result:
            return False

    # Check upwards
    temp_y = y
    while temp_y < N:
        temp_y += 1
        if [x, temp_y] in result:
            return False

    return True


RESULTS = []


def compute(x: int, y: int):
    """Compute queens

    Args:
        x (int): x
        y (int): y
    """

    # For each starting point
    for big_y in range(N):
        y = big_y
        result = []
        index = 0

        # Check each possibility
        while y < N:
            x = 0
            # Check all cells in x axis
            while y < N and x < N:
                # print(x, y)
                if diagonal(result, x, y) and vertical(result, x, y):
                    result.append([x, y])
                    # print(result)
                    y = 0
                    x += 1
                elif y == (N - 1):
                    # Backtrack
                    # print("Backtracking", result)
                    prev = result[-1]
                    if prev[1] + 1 == N:
                        while len(result) > 0:
                            result.pop()
                            if len(result) == 0:
                                y += 1
                                break
                            x = result[-1][0]
                            y = result[-1][1] + 1
                            if y < N:
                                break
                    else:
                        y = prev[1] + 1
                        x = prev[0]
                        result.pop()
                else:
                    y += 1

            # Check that each horizontal axis has a queen
            if len(result) == N:
                # print("Appending", result)
                if result not in RESULTS:
                    RESULTS.append(result)

                    # Increase index
                    index += 1
                    # Recompute result and update x, y
                    result = result[0:index + 1]
                    x = result[-1][0]
                    y = result[-1][1] + 1
                if index >= N - 1 or (x == N - 1 and y == N - 1):
                    break
            else:
                break
            y += 1


compute(0, 0)
for result in RESULTS:
    print(result)
