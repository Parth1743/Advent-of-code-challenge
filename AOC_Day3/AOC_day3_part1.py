import re


def calculate_sum_of_muls(memory):
    # Use a compiled regular expression for better performance
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    # Find all matches and compute the total in one step
    return sum(int(x) * int(y) for x, y in pattern.findall(memory))


if __name__ == "__main__":
    # Read the input file
    with open(r"input.txt", "r") as file:
        corrupted_memory = file.read()

    # Compute the result
    result = calculate_sum_of_muls(corrupted_memory)
    print("The sum of all valid multiplications is:", result)