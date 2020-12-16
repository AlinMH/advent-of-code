import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        intervals = []

        for idx, line in enumerate(lines):
            if line:
                _, rhs = line.split(": ")
                first, second = rhs.split(" or ")
                intervals.append(tuple(map(int, first.split("-"))))
                intervals.append(tuple(map(int, second.split("-"))))
            else:
                break

        numbers = []
        for line in lines[idx + 5:]:
            numbers.extend(map(int, line.split(",")))

        s = 0

        for n in numbers:
            ok = False
            for low, high in intervals:
                if low <= n <= high:
                    ok = True
                    break

            if not ok:
                s += n

        return s


if __name__ == "__main__":
    result = part1()
    print(result)
