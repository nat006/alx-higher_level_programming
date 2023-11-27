#!/usr/bin/python3

"""
This program solves the N queens puzzle.
"""

import sys

def solve_nqueens(N):
    """
    This function solves the N queens puzzle and prints all the solutions.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    backtrack(board, 0, solutions)
    
    for solution in solutions:
        print_solution(solution)

def backtrack(board, col, solutions):
    """
    Backtracking function to find all possible solutions to the N queens puzzle.
    """
    N = len(board)
    
    if col >= N:
        solutions.append(board)
        return
    
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            backtrack(board, col + 1, solutions)
            board[i][col] = 0

def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position on the board.
    """
    N = len(board)
    
    # Check rows and columns
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    
    # Check diagonals
    for i in range(N):
        for j in range(N):
            if (i + j == row + col or i - j == row - col) and board[i][j] == 1:
                return False
    
    return True

def print_solution(board):
    """
    Print a solution to the N queens puzzle.
    """
    N = len(board)
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end=" ")
    
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_nqueens(N)
