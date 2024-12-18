from collections import Counter
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def part1(l1: list, l2: list):
    l1.sort()
    l2.sort()

    sum_diff = 0

    for i in range(0, len(l1)):
        sum_diff += abs(l1[i] - l2[i])
        print(f"iter {i}: {sum_diff}")

    print(sum_diff)


def part2(l1: list, l2: list):
    counter = Counter(l2)
    counter_sum = 0

    for i in l1:
        counter_sum += i * counter[i]

    print(counter_sum)


if __name__ == "__main__":
    l1 = []
    l2 = []

    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            num1, num2 = line.strip().split("  ")
            l1.append(int(num1))
            l2.append(int(num2))

    part1(l1, l2)
    part2(l1, l2)
