#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    for row in board:
        line = "." * row + "Q" + "." * (len(board) - row - 1)
        print(line)

def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board)
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)

