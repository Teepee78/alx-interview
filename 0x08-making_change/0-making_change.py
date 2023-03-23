#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Determines the fewest number of coins to make total"""

    if total == 0:
        return 0
    if len(coins) == 0 or coins is None:
        return -1

    sorted_coins = [x for x in reversed(sorted(coins))]
    sum = 0
    count = 0

    for coin in sorted_coins:
        while sum < total and (total - sum) >= coin:
            sum += coin
            count += 1

    if sum == total:
        return count
    return -1
