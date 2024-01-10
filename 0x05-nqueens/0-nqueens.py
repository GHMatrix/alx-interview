#!/usr/bin/python3
"""
N Queens problem solver
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for prev_row in range(row):
        if (
            board[prev_row] == col
            or board[prev_row] == col - (row - prev_row)
            or board[prev_row] == col + (row - prev_row)
        ):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """
    Recursive function to solve N Queens problem
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)


def print_solutions(N, solutions):
    """
    Print the solutions in the required format
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_nqueens(N, 0, board, solutions)
    print_solutions(N, solutions)
