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

def bfs_score(grid, start):
    """Performs BFS from the start position to find reachable height-9 positions."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    reachable_nines = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # If we find a height-9 position, add it to reachable_nines
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            continue
        
        # Add neighbors with a height exactly 1 greater than the current position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append((nr, nc))
    
    return len(reachable_nines)

def calculate_trailhead_scores(file_path):
    """Reads the map from a file and calculates the sum of scores for all trailheads."""
    with open(file_path, 'r') as f:
        map_str = f.read()
    grid = parse_map(map_str)
    trailheads = find_trailheads(grid)
    total_score = sum(bfs_score(grid, trailhead) for trailhead in trailheads)
    return total_score

# Example usage
file_path = r"Input.txt"  # Replace with the path to your input file
print(calculate_trailhead_scores(file_path))
