from collections import defaultdict, deque


def parse_input(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    
    rules = []
    updates = []
    parsing_updates = False

    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))
    
    return rules, updates


def is_update_ordered(update, rules):
    position_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in position_map and y in position_map:
            if position_map[x] >= position_map[y]:
                return False
    return True


def topological_sort(pages, rules):
    # Build graph and in-degree
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform topological sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages


def find_middle_page(update):
    n = len(update)
    return update[n // 2]


def main():
    file_path = r"C:\Users\Parth garg\Documents\GitHub\Advent-of-code-challenge\AOC_Day5\input.txt"  # Replace with your input file path
    rules, updates = parse_input(file_path)
    
    ordered_updates = []
    unordered_updates = []
    
    for update in updates:
        if is_update_ordered(update, rules):
            ordered_updates.append(update)
        else:
            unordered_updates.append(update)
    
    # Reorder incorrectly-ordered updates
    corrected_updates = [
        topological_sort(update, rules) for update in unordered_updates
    ]
    
    # Calculate the sum of middle pages for corrected updates
    middle_page_sum = sum(find_middle_page(update) for update in corrected_updates)
    
    print("Sum of middle pages of corrected updates:", middle_page_sum)


if __name__ == "__main__":
    main()
