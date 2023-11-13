def is_valid(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True


def sudoku_solver(puzzle):
    empty_pos = find_empty_position(puzzle)

    if not empty_pos:
        return True

    row, col = empty_pos

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            if sudoku_solver(puzzle):
                return True
            puzzle[row][col] = 0

    return False


def find_empty_position(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return None


def sudoku(puzzle):
    puzzle_copy = [row[:] for row in puzzle]

    if sudoku_solver(puzzle_copy):
        return puzzle_copy
    else:
        return "No solution exists."