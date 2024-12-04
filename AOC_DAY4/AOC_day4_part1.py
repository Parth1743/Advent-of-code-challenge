def count_word_occurrences(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Define the directions (row_change, col_change)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1),  # Diagonal up-left
    ]

    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def search_from_position(row, col, direction):
        for i in range(word_length):
            r, c = row + i * direction[0], col + i * direction[1]
            if not is_valid_position(r, c) or grid[r][c] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if search_from_position(i, j, direction):
                    count += 1

    return count


# Read the grid from a file
def read_grid_from_file(file_path):
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]
    return grid


# Main function
if __name__ == "__main__":
    file_path = "input.txt"  # Replace with your file path
    grid = read_grid_from_file(file_path)
    result = count_word_occurrences(grid)
    print("The word XMAS appears", result, "times.")