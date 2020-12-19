import os
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def solve(part2=False):
    with open(INPUT_FILE, "r") as fp:
        table, strings = fp.read().split("\n\n")
        rules = dict(re.findall("(\d+):(.+)", table))

        if part2:
            # Special rules for part 2
            rules["8"] = "42+"
            rules["11"] = "|".join("42 " * i + "31 " * i for i in range(1, 10))

        while len(rules) > 1:
            # Find a "completed" rule to substitute
            k, v = next((k, v) for k, v in rules.items() if not re.search("\d", v))
            rules = {k1: re.sub(rf"\b{k}\b", f"({v})", v1) for k1, v1 in rules.items() if k1 != k}

        # Trim " and spaces, and add being/end markers.
        reg = re.compile("^" + re.sub('[ "]', "", rules["0"]) + "$")

        return sum(bool(reg.match(line)) for line in strings.split())


if __name__ == "__main__":
    result = solve()
    print(result)

    result = solve(part2=True)
    print(result)
