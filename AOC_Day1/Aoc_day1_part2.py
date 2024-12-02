from collections import Counter

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

# Function to calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count.get(number, 0)
    
    return similarity_score

# Main function
def main():
    print("Enter the left and right lists in two-column format (e.g.,):")
    print("3   4")
    print("4   3")
    print("2   5")
    print("Type 'done' when you're finished.")
    
    input_text = []
    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        input_text.append(line)
    
    input_data = "\n".join(input_text)
    left_list, right_list = parse_input(input_data)
    
    # Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    
    print("\nSimilarity Score:", similarity_score)

# Run the program
if __name__ == "__main__":
    main()
