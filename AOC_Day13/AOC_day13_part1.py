from math import gcd

def solve_claw_machine(machines):
    def solve_machine(a_x, a_y, b_x, b_y, p_x, p_y):
        # Use extended Euclidean algorithm to find integer solutions
        solutions = []
        for k_A in range(101):  # Limit k_A as per the problem
            x_remain = p_x - k_A * a_x
            y_remain = p_y - k_A * a_y

            if x_remain % b_x == 0 and y_remain % b_y == 0:
                k_B_x = x_remain // b_x
                k_B_y = y_remain // b_y

                if k_B_x == k_B_y and k_B_x >= 0:  # Both equations should agree
                    k_B = k_B_x
                    cost = 3 * k_A + k_B
                    solutions.append((k_A, k_B, cost))

        return min(solutions, key=lambda x: x[2]) if solutions else None

    total_cost = 0
    prizes_won = 0

    for machine in machines:
        a_x, a_y = machine['A']
        b_x, b_y = machine['B']
        p_x, p_y = machine['Prize']

        result = solve_machine(a_x, a_y, b_x, b_y, p_x, p_y)
        if result:
            _, _, cost = result
            total_cost += cost
            prizes_won += 1

    return prizes_won, total_cost

# Input parsing
def parse_input(input_text):
    machines = []
    for block in input_text.strip().split("\n\n"):
        lines = block.split("\n")
        a_x, a_y = map(int, lines[0].replace("Button A: X+", "").replace(" Y+", "").split(","))
        b_x, b_y = map(int, lines[1].replace("Button B: X+", "").replace(" Y+", "").split(","))
        p_x, p_y = map(int, lines[2].replace("Prize: X=", "").replace(" Y=", "").split(","))
        machines.append({"A": (a_x, a_y), "B": (b_x, b_y), "Prize": (p_x, p_y)})
    return machines

# Example usage
if __name__ == "__main__":
    with open(r"input.txt", "r") as file:
        input_text = file.read()
    
    machines = parse_input(input_text)
    prizes_won, total_cost = solve_claw_machine(machines)
    print(f"Prizes won: {prizes_won}, Total cost: {total_cost}")
