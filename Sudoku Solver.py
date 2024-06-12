def print_grid(grid):
    """Display the Sudoku grid in an easy-to-read format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(grid, row, col, num):
    """Verify if placing a number in a specific position is allowed."""
    for i in range(9):
        # Check the row and column
        if grid[row][i] == num or grid[i][col] == num:
            return False
        # Check the 3x3 sub-grid
        if grid[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using a backtracking approach."""
    for row in range(9):
        for col in range(9):
            # Look for an empty cell
            if grid[row][col] == 0:
                # Attempt to place digits 1-9
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        # Recursively solve the grid
                        if solve_sudoku(grid):
                            return True
                        # If not solvable, backtrack
                        grid[row][col] = 0
                return False
    return True

def reset_sudoku(grid):
    """Reverse the solved Sudoku by resetting solved cells."""
    for row in range(9):
        for col in range(9):
            # Find non-empty cells
            if grid[row][col] != 0:
                # Clear the cell
                grid[row][col] = 0
                # Attempt to reverse the grid
                if not solve_sudoku(grid):
                    return True
                # If unable to reverse, restore cell and continue
                grid[row][col] = grid[row][col]
    return False

def main():
    # Different Sudoku puzzle example (0 indicates empty cells)
    sudoku_grid = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

    print("Initial Sudoku grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSudoku grid after solving:")
        print_grid(sudoku_grid)
    else:
        print("No solution could be found")

    print("\nResetting the solution:")
    if reset_sudoku(sudoku_grid):
        print("\nSudoku grid after reset:")
        print_grid(sudoku_grid)
    else:
        print("Resetting the solution was not successful")

if __name__ == "__main__":
    main()
