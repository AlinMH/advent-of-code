import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def part1(matrix: list[list[str]]):
    num_safe = 0

    for row in matrix:
        row = [int(x) for x in row]
        print(row)
        if is_safe(row):
            num_safe += 1

    print(num_safe)


def is_safe(row: list[int]) -> bool:
    prev = row[0]
    crt = row[1]
    is_trend_asc = True
    if prev < crt:
        is_trend_asc = True
    elif prev > crt:
        is_trend_asc = False
    else:
        return False

    for i in range(0, len(row) - 1):
        prev = row[i]
        crt = row[i + 1]

        dif = crt - prev
        if abs(dif) > 3:
            return False
        if is_trend_asc and dif <= 0:
            return False
        elif not is_trend_asc and dif >= 0:
            return False

    return True


def is_safe2(row: list[int]) -> bool:
    res = is_safe(row)
    if res:
        return True

    for i in range(0, len(row)):
        res = is_safe(row[:i] + row[i + 1 :])
        if res:
            return True

    return False


def part2(matrix: list[list[str]]):
    num_safe = 0

    for row in matrix:
        row = [int(x) for x in row]
        print(row)
        if is_safe2(row):
            print("IS SAFE")
            num_safe += 1

    print(num_safe)


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as file:
        matrix = [list(line.split(" ")) for line in file]

    part2(matrix)
