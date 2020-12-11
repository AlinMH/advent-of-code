from copy import deepcopy

INPUT_FILE = "input"


def num_adj_occ1(i, j, mat):
    max_i = len(mat) - 1
    max_j = len(mat[0]) - 1

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    num = 0

    for dx, dy in directions:
        xp, yp = i + dx, j + dy
        if (xp >= 0 and xp <= max_i) and (yp >= 0 and yp <= max_j):
            view = mat[xp][yp]
            if view != ".":
                if view == "#":
                    num += 1
            xp += dx
            yp += dy

    return num



def num_adj_occ2(i, j, mat):
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
                    elif column == "L" and num_adj_occ1(i, j, prev) == 0:
                        current[i][j] = "#"
                    elif column == "#" and num_adj_occ1(i, j, prev) >= 4:
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
                    elif column == "L" and num_adj_occ2(i, j, prev) == 0:
                        current[i][j] = "#"
                    elif column == "#" and num_adj_occ2(i, j, prev) >= 5:
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
    result = part1()
    print(result)

    result = part2()
    print(result)
