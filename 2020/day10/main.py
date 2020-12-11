import os
INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")

def part1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        numbers = set(map(int, lines))

        current = 0
        ranges = [1, 3]

        ones = 0
        threes = 0

        while numbers:
            for r in ranges:
                if current + r in numbers:
                    current += r
                    if r == 1:
                        ones += 1
                    elif r == 3:
                        threes += 1

                    numbers.remove(current)
                    break

        return ones * (threes + 1)


def part2():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        numbers = list(map(int, lines))

        numbers.append(0)
        numbers.sort()
        numbers.append(numbers[-1] + 3)

        arrangements = [1]

        for i in range(1, len(numbers)):
            arrange = arrangements[i - 1]
            j = i - 2

            while j >= 0 and numbers[i] - numbers[j] <= 3:
                arrange += arrangements[j]
                j -= 1

            arrangements.append(arrange)

        return arrangements[-1]


if __name__ == "__main__":
    part1 = part1()
    print(part1)

    part2 = part2()
    print(part2)
