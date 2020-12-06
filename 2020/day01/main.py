INPUT_FILE = "input"
TARGET_YEAR = 2020


def part_1():
    with open(INPUT_FILE, "r") as fp:
        s = set(map(lambda x: int(x), fp))

        for elem in s:
            if TARGET_YEAR - elem in s:
                return elem * (TARGET_YEAR - elem)


def part_2():
    with open(INPUT_FILE, "r") as fp:
        s = set(map(lambda x: int(x), fp))

        for i in s:
            for j in s:
                if TARGET_YEAR - (i + j) in s:
                    return i * j * (TARGET_YEAR - (i + j))


if __name__ == "__main__":
    result = part_1()
    print(result)
    result = part_2()
    print(result)
