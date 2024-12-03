import re


def calculate_sum_of_muls(memory):
    # Use a compiled regular expression for better performance
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    # Initially, mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    # Split the memory into tokens and process each
    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", memory)
    for token in tokens:
        token = token.strip()
        if not token:
            continue

        if do_pattern.fullmatch(token):
            mul_enabled = True
        elif dont_pattern.fullmatch(token):
            mul_enabled = False
        elif mul_enabled and mul_pattern.fullmatch(token):
            x, y = map(int, mul_pattern.match(token).groups())
            total_sum += x * y

    return total_sum


if __name__ == "__main__":
    # Read the input file
    with open(r"input.txt", "r") as file:
        corrupted_memory = file.read()

    # Compute the result
    result = calculate_sum_of_muls(corrupted_memory)
    print("The sum of all valid multiplications is:", result)