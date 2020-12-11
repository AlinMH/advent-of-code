import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()

        preamables = []
        numbers = list(map(int, lines))
        available_numbers = list(range(1, 26))

        for n in numbers:
            s = set(preamables[-25:] + available_numbers)
            found = False

            for i in s:
                for j in s:
                    if i != j and i + j == n:
                        found = True

            if not found:
                return n

            preamables.append(n)


def part2(part1_ans):
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        numbers = list(map(int, lines))

        for idx, n in enumerate(numbers):
            current = [n]
            next = idx + 1

            while sum(current) < part1_ans:
                current.append(numbers[next])
                next += 1

            if len(current) >= 2 and sum(current) == part1_ans:
                return min(current) + max(current)


if __name__ == "__main__":
    part1 = part1()
    print(part1)

    part2 = part2(part1)
    print(part2)
