def calculate_total_fencing_price(map_file):
    from collections import deque

    with open(map_file, 'r') as file:
        map_grid = [list(line.strip()) for line in file]

    rows, cols = len(map_grid), len(map_grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def get_neighbors(r, c):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            yield nr, nc

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        plant_type = map_grid[r][c]

        area = 0
        perimeter = 0

        while queue:
            cr, cc = queue.popleft()
            area += 1

            for nr, nc in get_neighbors(cr, cc):
                if in_bounds(nr, nc):
                    if map_grid[nr][nc] == plant_type and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                    elif map_grid[nr][nc] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = bfs(r, c)
                total_price += area * perimeter

    return total_price

# Example Usage
map_file = r"input.txt"  # Replace with the path to your input file
print(calculate_total_fencing_price(map_file))
