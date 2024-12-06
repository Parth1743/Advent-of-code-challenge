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


def find_middle_page(update):
    n = len(update)
    return update[n // 2]


def main():
    file_path = r"input.txt"  # Replace with your input file path
    rules, updates = parse_input(file_path)
    
    correctly_ordered_updates = [
        update for update in updates if is_update_ordered(update, rules)
    ]
    
    middle_page_sum = sum(find_middle_page(update) for update in correctly_ordered_updates)
    
    print("Sum of middle pages of correctly-ordered updates:", middle_page_sum)


if __name__ == "__main__":
    main()
