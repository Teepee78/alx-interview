#!/usr/bin/python3
"""Find the winner of a prime game"""


def isPrime(number):
    """Checks if number is a prime number

    Args:
        number (int): number

    Returns:
        bool: true if number is a prime number, false otherwise
    """

    if number == 1:
        return False

    for i in range(number):
        for j in range(number):
            if i * j == number:
                return False

    return True


def getPrimeNumbers(number):
    """Get the lowest prime number less than number

    Args:
        number (int): number

    Returns:
        list[int]: list of prime numbers
    """

    for num in range(number):
        if isPrime(num):
            return num

    return None


def getWinner(name):
    """Get winner based on who's turn it is"""
    if name == "Maria":
        return "Ben"
    else:
        return "Maria"


def roundWinner(array):
    """Determine winner of round"""
    copyArray = array.copy()

    turn = "Maria"
    winner = turn

    while True:
        array = copyArray
        # Pick prime number
        prime = None
        for num in copyArray:
            if isPrime(num):
                prime = num
        # Check if a number could be picked
        if prime is None:
            return getWinner(turn)

        # Remove multiples of number that was picked
        for i in array:
            if i % prime == 0:
                copyArray.pop(copyArray.index(i))

        if turn == "Maria":
            turn = "Ben"
        else:
            turn = "Maria"

    return winner


def isWinner(x, nums):
    """Determine the winner of a prime game between Maria and Ben

    Args:
        x (int): number of rounds
        nums (list[int]): array of integers

    Returns:
        str | None: the winner, or None
    """

    score = {"Maria": 0, "Ben": 0}

    for i in range(x):
        number = nums[i]
        array = [num for num in range(number + 1) if num > 0]
        winner = roundWinner(array)
        score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Maria"] < score["Ben"]:
        return "Ben"

    return None
