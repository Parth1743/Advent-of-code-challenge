import sys
import pyperclip as pc


def pr(s):
    print(s)
    pc.copy(s)


sys.setrecursionlimit(10**6)

# File input handling
infile = (
    sys.argv[1]
    if len(sys.argv) > 1
    else r"input.txt"
)
with open(infile) as f:
    G = f.read().strip().split("\n")

R, C = len(G), len(G[0])
p1, p2 = 0, 0

# Find starting point
for r in range(R):
    for c in range(C):
        if G[r][c] == "^":
            sr, sc = r, c

# Directions: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Process each cell in the grid
for o_r in range(R):
    for o_c in range(C):
        r, c = sr, sc
        d = 0  # Starting direction
        SEEN = set()
        SEEN_RC = set()

        while True:
            if (r, c, d) in SEEN:
                p2 += 1
                break
            SEEN.add((r, c, d))
            SEEN_RC.add((r, c))

            dr, dc = DIRECTIONS[d]
            rr, cc = r + dr, c + dc

            if not (0 <= rr < R and 0 <= cc < C):
                if G[o_r][o_c] == "#":
                    p1 = len(SEEN_RC)
                break

            if G[rr][cc] == "#" or (rr == o_r and cc == o_c):
                d = (d + 1) % 4
            else:
                r, c = rr, cc

pr(p1)
pr(p2)