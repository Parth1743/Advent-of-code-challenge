from collections import deque

def parse_map(map_str):
    """Converts a map string into a 2D list of integers."""
    return [list(map(int, line.strip())) for line in map_str.strip().split('\n')]

def find_trailheads(grid):
    """Finds all positions with height 0 in the grid."""
    trailheads = []
    for r, row in enumerate(grid):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def dfs_count_paths(grid, r, c, memo):
    """
    Counts the number of distinct hiking trails starting from (r, c) using DFS with memoization.
    """
    rows, cols = len(grid), len(grid[0])

    # If the current position is a height-9, this is the end of a valid trail
    if grid[r][c] == 9:
        return 1

    # Check memoization table
    if (r, c) in memo:
        return memo[(r, c)]

    total_paths = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Ensure within bounds and that the height increases exactly by 1
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] + 1:
            total_paths += dfs_count_paths(grid, nr, nc, memo)

    # Store result in memoization table
    memo[(r, c)] = total_paths
    return total_paths

def calculate_trailhead_ratings(file_path):
    """
    Reads the map from a file and calculates the sum of ratings for all trailheads.
    """
    with open(file_path, 'r') as f:
        map_str = f.read()
    grid = parse_map(map_str)
    trailheads = find_trailheads(grid)

    total_rating = 0
    memo = {}
    for trailhead in trailheads:
        total_rating += dfs_count_paths(grid, trailhead[0], trailhead[1], memo)
    
    return total_rating

# Example usage
file_path = r"Input.txt"  # Replace with the path to your input file
print(calculate_trailhead_ratings(file_path))
