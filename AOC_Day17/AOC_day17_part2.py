import sys
import re
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

# Input handling
infile = sys.argv[1] if len(sys.argv) >= 2 else r'C:\Users\Parth garg\Documents\GitHub\Advent-of-code-challenge\AOC_Day17\input.txt'
ans = 0
D = open(infile).read().strip()

# Parsing the input
regs, program = D.split('\n\n')
A, B, C = ints(regs)
program = program.split(':')[1].strip().split(',')
program = [int(x) for x in program]

def run(Ast, part2):
    def getCombo(x):
        if x in [0, 1, 2, 3]:
            return x
        if x == 4:
            return A
        if x == 5:
            return B
        if x == 6:
            return C
        return -1  # Default fallback for invalid values

    A = Ast
    B = 0
    C = 0
    ip = 0
    out = []

    while ip < len(program):
        cmd = program[ip]
        op = program[ip + 1]
        combo = getCombo(op)

        if cmd == 0:
            A = A // 2**combo
            ip += 2
        elif cmd == 1:
            B = B ^ op
            ip += 2
        elif cmd == 2:
            B = combo % 8
            ip += 2
        elif cmd == 3:
            if A != 0:
                ip = op
            else:
                ip += 2
        elif cmd == 4:
            B = B ^ C
            ip += 2
        elif cmd == 5:
            out.append(int(combo % 8))
            if part2 and out[-1] != program[-1]:
                return out
            ip += 2
        elif cmd == 6:
            B = A // 2**combo
            ip += 2
        elif cmd == 7:
            C = A // 2**combo
            ip += 2
        else:
            print(f"Invalid command {cmd} at position {ip}")
            break

    return out

# Part 1
part1 = run(A, False)
print("Part 1 Output:", ','.join([str(x) for x in part1]))

# Part 2
Ast = 0
best = 0
found = False

while not found:
    Ast += 1
    A = Ast * 8**9 + 0o676236017
    out = run(A, True)
    
    # Debugging logs
    print(f"Testing Ast={Ast}, A={A}, Current Output={out}, Best Output Length={best}")

    if out == program:
        print("Match Found:", A)
        found = True
    elif len(out) > best:
        print(f"New Best Length Found: {len(out)}")
        best = len(out)

print("Final Result:", A)
