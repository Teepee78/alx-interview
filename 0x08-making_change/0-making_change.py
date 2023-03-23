#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Determines the fewest number of coins to make total"""

    if total == 0:
        return 0

    sorted_coins = [x for x in reversed(sorted(coins))]
    sum = 0
    count = 0

    for coin in sorted_coins:
        # print(f"sum: {sum}, coin: {coin}, remainder: {total - sum}")
        # print(count)
        while sum < total and (total - sum) >= coin:
            # print(f"{sum} + {coin}", end=" ")
            sum += coin
            # print(f"equal to {sum}")
            count += 1
            # print(f"sum: {sum}")

    if sum == total:
        return count
    return -1
