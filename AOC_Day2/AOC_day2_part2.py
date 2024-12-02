def is_safe(report):
    """
    Determines if a single report is safe without removing any level.
    """
    n = len(report)
    if n < 2:
        return True  # A single level is trivially safe.

    increasing = all(report[i] > report[i - 1] for i in range(1, n))
    decreasing = all(report[i] < report[i - 1] for i in range(1, n))
    valid_differences = all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, n))
    
    return (increasing or decreasing) and valid_differences


def is_safe_with_dampener(report):
    """
    Determines if a report is safe with the Problem Dampener.
    """
    if is_safe(report):
        return True  # Already safe.

    n = len(report)
    for i in range(n):
        # Remove the i-th level and check if the remaining report is safe
        reduced_report = report[:i] + report[i+1:]
        if is_safe(reduced_report):
            return True

    return False  # Not safe even with one level removed.


def count_safe_reports(reports):
    """
    Counts the number of safe reports considering the Problem Dampener.
    """
    return sum(is_safe_with_dampener(report) for report in reports)


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
