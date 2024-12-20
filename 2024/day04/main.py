import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

PATTERNS = ("XMAS", "SAMX")


def part1(matrix: list[list[str]]):
    num_matches = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # 4 directions
            for pattern in PATTERNS:
                num_matches += check_pattern(matrix, i, j, pattern)
    print(num_matches)


def part2(matrix: list[list[str]]):
    num_matches = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            num_matches += check_pattern2(matrix, i, j)
    print(num_matches)


def check_pattern(matrix: list[list[str]], i: int, j: int, pattern: str) -> int:
    count = 0
    if (
        j + 3 < len(matrix[0])
        and matrix[i][j] == pattern[0]
        and matrix[i][j + 1] == pattern[1]
        and matrix[i][j + 2] == pattern[2]
        and matrix[i][j + 3] == pattern[3]
    ):
        count += 1
    if (
        i + 3 < len(matrix)
        and matrix[i][j] == pattern[0]
        and matrix[i + 1][j] == pattern[1]
        and matrix[i + 2][j] == pattern[2]
        and matrix[i + 3][j] == pattern[3]
    ):
        count += 1

    if (
        i + 3 < len(matrix)
        and j + 3 < len(matrix[0])
        and matrix[i][j] == pattern[0]
        and matrix[i + 1][j + 1] == pattern[1]
        and matrix[i + 2][j + 2] == pattern[2]
        and matrix[i + 3][j + 3] == pattern[3]
    ):
        count += 1

    if (
        i + 3 < len(matrix)
        and j - 3 >= 0
        and matrix[i][j] == pattern[0]
        and matrix[i + 1][j - 1] == pattern[1]
        and matrix[i + 2][j - 2] == pattern[2]
        and matrix[i + 3][j - 3] == pattern[3]
    ):
        count += 1
    return count


def check_pattern2(matrix: list[list[str]], i: int, j: int) -> bool:
    first_check = (
        i + 2 < len(matrix)
        and j + 2 < len(matrix[0])
        and matrix[i][j] == "M"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j + 2] == "S"
    ) or (
        i + 2 < len(matrix)
        and j + 2 < len(matrix[0])
        and matrix[i][j] == "S"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j + 2] == "M"
    )
    if first_check:
        return (
            i + 2 < len(matrix)
            and j + 2 < len(matrix[0])
            and matrix[i][j + 2] == "M"
            and matrix[i + 1][j + 1] == "A"
            and matrix[i + 2][j] == "S"
        ) or (
            i + 2 < len(matrix)
            and j + 2 < len(matrix[0])
            and matrix[i][j + 2] == "S"
            and matrix[i + 1][j + 1] == "A"
            and matrix[i + 2][j] == "M"
        )

    return False


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
        matrix = [list(line.strip()) for line in lines]
        part2(matrix)
