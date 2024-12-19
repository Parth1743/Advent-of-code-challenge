def parse_input(input_data):
    # Split input into patterns and designs
    patterns_part, designs_part = input_data.strip().split('\n\n')
    patterns = patterns_part.split(', ')
    designs = designs_part.split('\n')
    return patterns, designs

def count_ways_to_construct_design(design, patterns):
    # Dynamic programming array to store the number of ways to construct each prefix
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Base case: one way to construct an empty prefix

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(design)]

def total_ways_to_construct_all_designs(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_construct_design(design, patterns)
    return total_ways

def main():
    # Read input from a file
    with open(r'input.txt', 'r') as file:
        input_data = file.read()

    patterns, designs = parse_input(input_data)

    # Calculate the total number of ways to construct all designs
    result = total_ways_to_construct_all_designs(patterns, designs)

    print(result)

if __name__ == "__main__":
    main()
