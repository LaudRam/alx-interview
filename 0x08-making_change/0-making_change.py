#!/usr/bin/python3
""" making change module """


def makeChange(coins, total):
    """ change money with the least amount of coins """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    index, number_coins = (0, 0)
    total_cpy = total
    len_coins = len(coins)

    while(index < len_coins and total_cpy > 0):
        if (total_cpy - coins[index]) >= 0:
            total_cpy -= coins[index]
            number_coins += 1
        else:
            index += 1

    check = total_cpy > 0 and number_coins > 0
    return -1 if check or number_coins == 0 else number_coins
