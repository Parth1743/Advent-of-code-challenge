from itertools import product

def evaluate_expression(nums, ops):
    """Evaluates the expression formed by nums and ops in left-to-right order."""
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
    return result

def is_solvable(target, nums):
    """Checks if target can be achieved by inserting operators between nums."""
    operators = ['+', '*']
    # Generate all possible combinations of operators
    for ops in product(operators, repeat=len(nums) - 1):
        if evaluate_expression(nums, ops) == target:
            return True
    return False

def calculate_total_calibration_from_file(filename):
    """Reads the input file and calculates the total calibration result."""
    total = 0
    with open(filename, "r") as file:
        for line in file:
            if ':' in line:
                target, nums_str = line.split(':')
                target = int(target.strip())
                nums = list(map(int, nums_str.strip().split()))
                if is_solvable(target, nums):
                    total += target
    return total

# Main Program
if __name__ == "__main__":
    # Specify the input file name
    input_file = r"input.txt"  # Replace with your file name

    # Calculate Total Calibration Result
    total_result = calculate_total_calibration_from_file(input_file)
    print("Total Calibration Result:", total_result)
