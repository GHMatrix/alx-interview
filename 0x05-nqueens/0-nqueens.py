#!/usr/bin/python3
"""Solving the N-queens challenge.
"""
import sys


def initialize_board(size):
    """Initialize a sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for i in range(size)]
    [row.append(' ') for i in range(size) for row in chess_board]
    return chess_board


def copy_board(original_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(original_board, list):
        return list(map(copy_board, original_board))
    return original_board


def get_solution(chess_board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chess_board)):
        for c in range(len(chess_board)):
            if chess_board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_out(chess_board, row, col):
    """Mark out spots on a chessboard."""
    for c in range(col + 1, len(chess_board)):
        chess_board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = "x"
    for r in range(row + 1, len(chess_board)):
        chess_board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        chess_board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(chess_board)):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess_board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(chess_board)):
        if c < 0:
            break
        chess_board[r][c] = "x"
        c -= 1


def recursively_solve(chess_board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    """
    if queens == len(chess_board):
        solutions.append(get_solution(chess_board))
        return solutions

    for col in range(len(chess_board)):
        if chess_board[row][col] == " ":
            tmp_board = copy_board(chess_board)
            tmp_board[row][col] = "Q"
            mark_out(tmp_board, row, col)
            solutions = recursively_solve(tmp_board, row + 1,
                                          queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = initialize_board(int(sys.argv[1]))
    solutions = recursively_solve(chess_board, 0, 0, [])
    for sol in solutions:
        print(sol)
