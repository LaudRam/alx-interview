#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.
"""

import sys


def nqueens(list):
    """the function accepts a list as a parameter"""
    try:
        if len(list[0]) != 2:
            print("Usage: nqueens N")
            exit(1)
        NxN = int(list[0][1])
        if NxN < 4:
            print("N must be at least 4")
            exit(1)
        col = list[1]
        listThreat = list[2]
        for row in range(NxN):
            nonAttack = 1
            for move in listThreat:
                if move[1] == row:
                    nonAttack = 0
                    break
                if col - row == move[0] - move[1]:
                    nonAttack = 0
                    break
                if row - move[1] == move[0] - col:
                    nonAttack = 0
                    break
            if nonAttack == 1:
                listThreat.append([col, row])
                if NxN - 1 != col:
                    nqueens([list[0], col + 1, listThreat])
                else:
                    print(listThreat)
                del listThreat[-1]
    except ValueError:
        print("N must be a number")
        exit(1)


nqueens([sys.argv, 0, []])
