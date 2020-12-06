INPUT_FILE = "input"


def calc_row(row_seq):
    low = 0
    high = 127

    for c in row_seq[:-1]:
        if c == "F":
            high -= round((high - low) / 2)
        else:
            low += round((high - low) / 2)

    if row_seq[-1] == "F":
        return low
    else:
        return high


def calc_col(col_seq):
    low = 0
    high = 7

    for c in col_seq[:-1]:
        if c == "L":
            high -= round((high - low) / 2)
        else:
            low += round((high - low) / 2)

    if col_seq[-1] == "L":
        return low
    else:
        return high


def calc_seat_id(seq):
    row_seq = seq[:7]
    col_seq = seq[7:]

    return calc_row(row_seq) * 8 + calc_col(col_seq)


def solve():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()
        seat_ids = []

        for line in lines:
            seat_ids.append(calc_seat_id(line[:-1]))

    sorted_seats = list(sorted(seat_ids))
    missing_seat = None

    for i in range(len(sorted_seats)):
        if sorted_seats[i + 1] - sorted_seats[i] != 1:
            missing_seat = sorted_seats[i + 1] - 1
            break

    return max(seat_ids), missing_seat


if __name__ == "__main__":
    part1, part2 = solve()
    print(part1)
    print(part2)
