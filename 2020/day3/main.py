from functools import reduce

INPUT_FILE = "PATH_TO_INPUT"

PART1_RIGHT = 3
PART2_DOWN = 1

PART2_SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def solve(right, down):
    trees = 0
    x, y = 0, 0

    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()
        while y < len(lines):
            if lines[y][x] == "#":
                trees += 1

            x = (x + right) % (len(lines[0]) - 1)
            y += down

    return trees


if __name__ == "__main__":
    result = solve(PART1_RIGHT, PART2_DOWN)
    print(result)

    result = []
    for right, down in PART2_SLOPES:
        result.append(solve(right, down))

    print(reduce(lambda x, y: x * y, result))
