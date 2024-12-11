from math import log, floor


class Solution:
    tracking = {}

    def blink(self, stone, times):
        if times == 0:
            return 1

        if (stone, times) in self.tracking:
            return self.tracking[(stone, times)]

        if stone == 0:
            size = self.blink(1, times - 1)
        elif (digits := (floor(log(stone, 10)) + 1)) % 2 < 1:
            left = stone // 10 ** (digits // 2)
            right = stone % 10 ** (digits // 2)
            size = self.blink(left, times - 1) + self.blink(right, times - 1)
        else:
            size = self.blink(stone * 2024, times - 1)

        if (stone, times) not in self.tracking:
            self.tracking[(stone, times)] = size

        return size

    def part1(self, data):
        stones = map(int, data[0].split())
        count = sum(self.blink(stone, 25) for stone in stones)
        return count

    def part2(self, data):
        stones = map(int, data[0].split())
        count = sum(self.blink(stone, 75) for stone in stones)
        return count

    def read_input_file(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.read_input_file(r"C:\Users\Parth garg\Documents\GitHub\Advent-of-code-challenge\AOC_Day11\input.txt")
    result_part1 = solution.part1(input_data)
    print("Part 1 Result:", result_part1)
    result_part2 = solution.part2(input_data)
    print("Part 2 Result:", result_part2)