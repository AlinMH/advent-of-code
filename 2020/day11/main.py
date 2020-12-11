from copy import deepcopy

INPUT_FILE = "input"


def are_adjancent(i, j, mat, seat_type):
    max_i = len(mat) - 1
    max_j = len(mat[0]) - 1

    up = mat[i - 1][j] == seat_type if i != 0 else True
    down = mat[i + 1][j] == seat_type if i != max_i else True
    left = mat[i][j - 1] == seat_type if j != 0 else True
    right = mat[i][j + 1] == seat_type if j != max_j else True
    up_left = mat[i - 1][j - 1] == seat_type if i != 0 and j != 0 else True
    up_right = mat[i - 1][j + 1] == seat_type if i != 0 and j != max_j else True
    down_left = mat[i + 1][j - 1] == seat_type if i != max_i and j != 0 else True
    down_right = mat[i + 1][j + 1] == seat_type if i != max_i and j != max_j else True

    flags = [up, down, left, right, up_left, up_right, down_left, down_right]

    return all(flags)


def num_adj_occ(i, j, mat):
    max_i = len(mat) - 1
    max_j = len(mat[0]) - 1

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    num = 0

    for dx, dy in directions:
        xp, yp = i + dx, j + dy
        while (xp >= 0 and xp <= max_i) and (yp >= 0 and yp <= max_j):
            view = mat[xp][yp]
            if view != ".":
                if view == "#":
                    num += 1
                break
            xp += dx
            yp += dy

    return num


def part1():
    with open(INPUT_FILE, "r") as fp:
        prev = list(map(list, fp.read().splitlines()))
        current = []
        current_round = 0

        while True:
            if not current:
                current = deepcopy(prev)

            for i, row in enumerate(prev):
                for j, column in enumerate(row):
                    if column == ".":
                        continue
                    elif are_adjancent(i, j, prev, column):
                        current[i][j] = "#" if column == "L" else "L"

            if prev == current:
                occupied = 0
                for row in current:
                    for column in row:
                        if column == "#":
                            occupied += 1
                return occupied

            current_round += 1
            prev = deepcopy(current)


def part2():
    with open(INPUT_FILE, "r") as fp:
        prev = list(map(list, fp.read().splitlines()))
        current = []
        current_round = 0

        while True:
            if not current:
                current = deepcopy(prev)

            for i, row in enumerate(prev):
                for j, column in enumerate(row):
                    if column == ".":
                        continue
                    elif column == "L" and num_adj_occ(i, j, prev) == 0:
                        current[i][j] = "#"
                    elif column == "#" and num_adj_occ(i, j, prev) >= 5:
                        current[i][j] = "L"

            if prev == current:
                occupied = 0
                for row in current:
                    for column in row:
                        if column == "#":
                            occupied += 1
                return occupied

            current_round += 1
            prev = deepcopy(current)


if __name__ == "__main__":
    # result = part1()
    # print(result)

    result = part2()
    print(result)
