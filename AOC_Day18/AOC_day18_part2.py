from collections import deque

def parse_input(input_data):
    # Parse the input list of byte positions
    positions = [tuple(map(int, line.split(','))) for line in input_data.strip().split('\n')]
    return positions

def simulate_falling_bytes(positions, grid_size=71):
    # Initialize the grid
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    return grid

def is_path_blocked(grid, start, goal):
    # BFS for path existence
    queue = deque([start])
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y = queue.popleft()

        # Check if we've reached the goal
        if (x, y) == goal:
            return False  # Path is still open

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return True  # Path is blocked

def find_blocking_byte(positions, grid_size=71):
    grid = simulate_falling_bytes(positions, grid_size)
    start = (0, 0)
    goal = (70, 70)

    for i, (x, y) in enumerate(positions):
        grid[y][x] = 1  # Corrupt this position

        if is_path_blocked(grid, start, goal):
            return f"{x},{y}"  # Return the blocking byte's coordinates

    return None  # No blocking byte found

def main():
    # Read input from a file
    with open(r'input.txt', 'r') as file:
        input_data = file.read()

    positions = parse_input(input_data)

    # Find the first byte that blocks the path to the exit
    result = find_blocking_byte(positions, grid_size=71)

    print(result)

if __name__ == "__main__":
    main()
