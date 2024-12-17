from heapq import heappop, heappush

def parse_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        maze = file.readlines()
    
    start = None
    end = None
    grid = []
    
    for y, line in enumerate(maze):
        grid.append(list(line.strip()))  # Strip to remove newline characters
        if "S" in line:
            start = (y, line.index("S"))
        if "E" in line:
            end = (y, line.index("E"))
    
    return grid, start, end

def bfs_lowest_score(file_path):
    grid, start, end = parse_maze_from_file(file_path)
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    dir_list = ['N', 'E', 'S', 'W']
    
    # Priority queue: (score, x, y, direction)
    queue = [(0, start[0], start[1], 'E')]
    visited = set()
    
    while queue:
        score, x, y, dir = heappop(queue)
        
        # If we reach the end, return the score
        if (x, y) == end:
            return score
        
        # Avoid revisiting states
        if (x, y, dir) in visited:
            continue
        visited.add((x, y, dir))
        
        # Move forward
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
            heappush(queue, (score + 1, nx, ny, dir))
        
        # Rotate (clockwise and counterclockwise)
        current_idx = dir_list.index(dir)
        for turn_cost, new_dir in [(1000, dir_list[(current_idx + 1) % 4]),  # Clockwise
                                   (1000, dir_list[(current_idx - 1) % 4])]:  # Counterclockwise
            heappush(queue, (score + turn_cost, x, y, new_dir))
    
    # If no path is found
    return -1

# Specify the path to the input file
file_path = r"input.txt"
print(bfs_lowest_score(file_path))
