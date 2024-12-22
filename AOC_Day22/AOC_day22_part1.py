def parse_input(input_data):
    # Parse input secret numbers from the input data
    return list(map(int, input_data.strip().split('\n')))

def generate_secret_number(secret):
    # Process the secret number according to the rules
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def get_2000th_secret(initial_secret):
    # Generate the 2000th secret number from the initial secret
    secret = initial_secret
    for _ in range(2000):
        secret = generate_secret_number(secret)
    return secret

def calculate_sum_of_2000th_secrets(secrets):
    # Calculate the sum of the 2000th secret numbers for all buyers
    total = 0
    for secret in secrets:
        total += get_2000th_secret(secret)
    return total

def main():
    # Read input from a file
    with open(r'input.txt', 'r') as file:
        input_data = file.read()

    # Parse input and calculate the result
    initial_secrets = parse_input(input_data)
    result = calculate_sum_of_2000th_secrets(initial_secrets)

    print(result)

if __name__ == "__main__":
    main()
