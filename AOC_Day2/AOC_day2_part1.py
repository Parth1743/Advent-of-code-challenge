def is_safe(report):
    """
    Determines if a single report is safe.
    """
    n = len(report)
    if n < 2:
        return True  # A single level is trivially safe.
    
    # Check if the report is strictly increasing or decreasing
    increasing = all(report[i] > report[i - 1] for i in range(1, n))
    decreasing = all(report[i] < report[i - 1] for i in range(1, n))
    
    # Check if all differences are within the range [1, 3]
    valid_differences = all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, n))
    
    return (increasing or decreasing) and valid_differences

def count_safe_reports(reports):
    """
    Counts the number of safe reports in the data.
    """
    return sum(is_safe(report) for report in reports)

def parse_input(input_text):
    """
    Parses the input text into a list of reports.
    """
    return [list(map(int, line.split())) for line in input_text.strip().split("\n")]

# Main function
def main():
    print("Enter all reports (multi-line input). Type 'done' when finished:")
    input_lines = []
    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        input_lines.append(line)
    
    input_text = "\n".join(input_lines)
    reports = parse_input(input_text)
    safe_count = count_safe_reports(reports)
    
    print("\nNumber of safe reports:", safe_count)

# Run the program
if __name__ == "__main__":
    main()
