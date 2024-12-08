from collections import defaultdict
from itertools import combinations

def parse_grid(file_path):
    """
    Parse the input file to create a grid.
    Each line of the file represents a row in the grid.
    """
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")

def in_bounds(x, y, n):
    """
    Check if the coordinates (x, y) are within the bounds of an n x n grid.
    """
    return 0 <= x < n and 0 <= y < n

def get_antinodes(a, b, n):
    """
    Calculate the antinodes for a pair of points a and b.
    Return antinodes that fall within grid bounds.
    """
    ax, ay = a
    bx, by = b
    
    # Calculate the positions of potential antinodes
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)
    
    # Yield antinodes if they are within bounds
    if in_bounds(cx, cy, n):
        yield (cx, cy)
    if in_bounds(dx, dy, n):
        yield (dx, dy)

def calculate_antinodes(grid):
    """
    Calculate the total number of unique antinodes in the grid.
    """
    n = len(grid)  # Grid size (assumed square)
    antinodes = set()
    all_locs = defaultdict(list)
    
    # Collect positions of all antennas by their frequency
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))
    
    # Calculate antinodes for each frequency
    for freq in all_locs:
        locs = all_locs[freq]
        for a, b in combinations(locs, r=2):
            for antinode in get_antinodes(a, b, n):
                antinodes.add(antinode)
    
    return len(antinodes)

if __name__ == "__main__":
    # Input file path
    file_path = r"input.txt"  # Replace with your input file path
    
    # Parse the grid from the input file
    grid = parse_grid(file_path)
    
    # Calculate and print the number of unique antinodes
    result = calculate_antinodes(grid)
    print("Total unique antinode locations:", result)
