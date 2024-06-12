# 📝 Task-04: Sudoku Solver 

Welcome to Task-04! This project is a Python-based Sudoku Solver that uses a backtracking algorithm to automatically solve Sudoku puzzles.

# Introduction
This repository contains a Python script to solve Sudoku puzzles programmatically and reset them back to their initial state after solving. Sudoku solving is achieved through a backtracking algorithm that systematically fills in the puzzle cells while adhering to Sudoku rules. The reset functionality attempts to undo the solved state, clearing cells to revert the puzzle to its original, unsolved condition.

# Features

     •	Input: Accepts an initial Sudoku grid where 0 represents empty cells.
     •	Output: Displays the completed Sudoku grid once solved.
     •	Solve Sudoku: Automatically solves Sudoku puzzles using a backtracking algorithm.
     •	Reset Sudoku: Reverts a solved Sudoku puzzle to its initial unsolved state.
     •	Print Grid: Displays the Sudoku grid in a readable format for easy visualization.

https://github.com/ChaimaBenAchiba/Sudoku_Solver/issues/1#issue-2349717474

# Implementation Details
•	Sudoku Grid: Represented as a 2D list in Python where 0 denotes empty cells.
•	Backtracking Algorithm: Utilized to fill in empty cells by recursively attempting possible numbers.
•	Helper Functions:
      *solve_sudoku(grid): Recursive function that solves the Sudoku puzzle.
      *find_empty_cell(grid): Helper function to find the next empty cell in the grid.
     * is_valid(grid, row, col, num): Checks if placing num at (row, col) is valid according to Sudoku rules.

