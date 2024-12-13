class Solution:
    def part1(self, data):
        machines = ("\n".join(data)).split("\n\n")
        coins = 0

        for machine in machines:
            btn_a, btn_b, prize = machine.split("\n")

            btn_a = [*map(lambda i: int(i[2:]), btn_a.split(": ")[1].split(", "))]
            btn_b = [*map(lambda i: int(i[2:]), btn_b.split(": ")[1].split(", "))]
            prize = [*map(lambda i: int(i[2:]), prize.split(": ")[1].split(", "))]

            # Calculate times_a and times_b
            times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (
                btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
            )
            times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]

            if (
                100 >= times_a >= 0
                and 100 >= times_b >= 0
                and times_a.is_integer()
                and times_b.is_integer()
            ):
                coins += int(times_a) * 3 + int(times_b)

        return coins

    def part2(self, data):
        machines = ("\n".join(data)).split("\n\n")
        coins = 0

        for machine in machines:
            btn_a, btn_b, prize = machine.split("\n")

            btn_a = [*map(lambda i: int(i[2:]), btn_a.split(": ")[1].split(", "))]
            btn_b = [*map(lambda i: int(i[2:]), btn_b.split(": ")[1].split(", "))]
            prize = [
                *map(
                    lambda i: int(i[2:]) + 10000000000000,
                    prize.split(": ")[1].split(", "),
                )
            ]

            # Calculate times_a and times_b
            times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (
                btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
            )
            times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]

            if times_a.is_integer() and times_b.is_integer():
                coins += int(times_a) * 3 + int(times_b)

        return coins



file_path = r"input.txt".strip()

# Read the data from the file
with open(file_path, "r") as f:
    data = [line.strip() for line in f.readlines()]

# Create an instance of the Solution class
solution = Solution()


print("Part 2:", solution.part2(data))