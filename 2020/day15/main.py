import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def solve(steps):
    with open(INPUT_FILE, "r") as fp:
        starting_numbers = list(map(int, fp.read().split(",")))
        mem = {n: idx + 1 for idx, n in enumerate(starting_numbers[:-1])}

        current_number = starting_numbers[-1]

        for round_no in range(len(starting_numbers), steps):
            mem[current_number], current_number = round_no, round_no - mem.get(
                current_number, round_no
            )

        return current_number


if __name__ == "__main__":
    result = solve(2020)
    print(result)

    result = solve(30000000)
    print(result)
