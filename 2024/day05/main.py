from collections import defaultdict
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def parse() -> tuple[dict[int, list[int]], list[list[int]]]:
    rules = defaultdict(list)
    f = open(INPUT_FILE)
    while (line := f.readline().strip()) != "":
        lhs, rhs = line.split("|")
        rules[int(lhs)].append(int(rhs))

    all_entries = f.readlines()
    entries = [list(map(int, entry.strip().split(","))) for entry in all_entries]

    return rules, entries


def check_rule_for_entry(rules: dict[int, list[int]], entry: list[int]) -> bool:
    for idx, elem in enumerate(entry):
        if idx + 1 == len(entry):
            return True

        for i in entry[idx + 1 :]:
            if i not in rules[elem]:
                return False


def part1(rules: dict[int, list[int]], entries: list[list[int]]) -> list[list[int]]:
    sum_middles = 0
    failed_entries = []

    for entry in entries:
        if check_rule_for_entry(rules, entry):
            sum_middles += entry[len(entry) // 2]
        else:
            failed_entries.append(entry)

    print(sum_middles)
    return failed_entries


def reorder_entry(rules: dict[int, list[int]], entry: list[int]) -> list[int]:
    """Reorder the entry so it checks the rules correctly."""
    while not check_rule_for_entry(rules, entry):
        for idx, elem in enumerate(entry):
            if idx + 1 == len(entry):
                break

            for i in entry[idx + 1 :]:
                if i not in rules[elem]:
                    entry.remove(i)
                    entry.insert(idx, i)
                    break
    return entry


def part2(rules: dict[int, list[int]], failed_entries: list[list[int]]):
    sum_middles = 0

    for entry in failed_entries:
        reordered_entry = reorder_entry(rules, entry)
        sum_middles += reordered_entry[len(reordered_entry) // 2]

    print(sum_middles)


if __name__ == "__main__":
    r, e = parse()
    failed_entries = part1(r, e)
    part2(r, failed_entries)

    print(failed_entries)
