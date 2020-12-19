import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()


if __name__ == "__main__":
    result = part1()
    print(result)
