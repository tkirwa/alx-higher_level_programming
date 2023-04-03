#!/usr/bin/env python3
import sys


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        return

    rows = set()
    cols = set()
    diagonals1 = set()
    diagonals2 = set()

    def backtrack(queens, row):
        if row == n:
            print(queens)
            return
        for col in range(n):
            if col in cols or row + col in diagonals1 or row - col in diagonals2:
                continue
            rows.add(row)
            cols.add(col)
            diagonals1.add(row + col)
            diagonals2.add(row - col)
            backtrack(queens + [[row, col]], row + 1)
            rows.remove(row)
            cols.remove(col)
            diagonals1.remove(row + col)
            diagonals2.remove(row - col)

    backtrack([], 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
