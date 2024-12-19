def parse_input(input_data):
    # Split input into patterns and designs
    patterns_part, designs_part = input_data.strip().split('\n\n')
    patterns = patterns_part.split(', ')
    designs = designs_part.split('\n')
    return patterns, designs

def can_construct_design(design, patterns):
    # Dynamic programming array
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: empty prefix is always constructible

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[len(design)]

def count_possible_designs(patterns, designs):
    count = 0
    for design in designs:
        if can_construct_design(design, patterns):
            count += 1
    return count

def main():
    # Read input from a file
    with open(r'input.txt', 'r') as file:
        input_data = file.read()

    patterns, designs = parse_input(input_data)

    # Count how many designs are possible
    result = count_possible_designs(patterns, designs)

    print(result)

if __name__ == "__main__":
    main()
