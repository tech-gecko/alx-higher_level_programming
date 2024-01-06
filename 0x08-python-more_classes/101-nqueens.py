#!/usr/bin/python3
import sys

def is_safe(board, row, col):
   """Checks if placing a queen at (row, col) is safe."""
   for i in range(row):
       if board[i][col] == 1 or abs(row - i) == abs(col - board[i].index(1)):
           return False
   return True

def solve_n_queens_util(board, row, n):
   """Recursively solves the N-Queens problem using backtracking."""
   if row == n:
       # Print the solution in the required format
       for i in range(n):
           print("".join('.' * j + 'Q' + '.' * (n - j - 1) for j in range(n) if board[i][j] == 1))
       print()
       return

   for col in range(n):
       if is_safe(board, row, col):
           board[row][col] = 1
           solve_n_queens_util(board, row + 1, n)
           board[row][col] = 0  # Backtrack

def solve_n_queens(n):
   """Starts the N-Queens problem solver."""
   board = [[0] * n for _ in range(n)]
   solve_n_queens_util(board, 0, n)

if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Usage: nqueens N", file=sys.stderr)
       sys.exit(1)

   try:
       n = int(sys.argv[1])
   except ValueError:
       print("N must be a number", file=sys.stderr)
       sys.exit(1)

   if n < 4:
       print("N must be at least 4", file=sys.stderr)
       sys.exit(1)

   solve_n_queens(n)
