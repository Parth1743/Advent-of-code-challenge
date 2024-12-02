# Function to parse input and split into left and right lists
def parse_input(input_text):
    left_list = []
    right_list = []
    lines = input_text.strip().split("\n")
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list

# Function to calculate the output
def process_lists(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the pairwise absolute differences
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance


# Main function
def main():
    print("Enter the left and right lists in two-column format (e.g.,):")
    print("45730   14776")
    print("85407   18493")
    print("Type 'done' when you're finished.")
    
    input_text = []
    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        input_text.append(line)
    
    input_data = "\n".join(input_text)
    left_list, right_list = parse_input(input_data)
    
    # Process the lists
    result = process_lists(left_list, right_list)
    
    print("\nProcessed Output:")
    print(result)

# Run the program
if __name__ == "__main__":
    main()
