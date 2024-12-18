from collections import deque

def parse_input(input_data):
    # Parse the input list of byte positions
    positions = [tuple(map(int, line.split(','))) for line in input_data.strip().split('\n')]
    return positions

def simulate_falling_bytes(positions, grid_size=71, max_bytes=1024):
    # Initialize the grid
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    # Mark the grid with falling bytes
    for i, (x, y) in enumerate(positions):
        if i >= max_bytes:
            break
        grid[y][x] = 1  # Corrupted

    return grid

def find_shortest_path(grid, start, goal):
    # BFS for shortest path
    queue = deque([(start, 0)])  # (current_position, steps)
    visited = set()
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        (x, y), steps = queue.popleft()

        # Check if we've reached the goal
        if (x, y) == goal:
            return steps

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1  # If no path is found

def main():
    # Read input from a file
    with open(r'input.txt', 'r') as file:
        input_data = file.read()

    positions = parse_input(input_data)

    # Simulate the first kilobyte (1024 bytes) falling onto the memory space
    grid = simulate_falling_bytes(positions, grid_size=71, max_bytes=1024)

    # Find the shortest path from (0, 0) to (70, 70)
    start = (0, 0)
    goal = (70, 70)
    result = find_shortest_path(grid, start, goal)

    print(result)

if __name__ == "__main__":
    main()
