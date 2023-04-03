#!/usr/bin/python3
import sys


def is_valid(board, row, col, n):
    """
    Check if it is valid to place a queen at board[row][col] given the current state of the board
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col, n):
    """
    Solve N Queen problem
    """
    if col >= n:
        # All queens are placed, print the solution
        print([[i, j] for i in range(n) for j in range(n) if board[i][j] == 1])
        return True

    for i in range(n):
        if is_valid(board, i, col, n):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve(board, col + 1, n)

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for x in range(n)] for y in range(n)]
    solve(board, 0, n)
