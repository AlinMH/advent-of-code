from functools import reduce
from collections import defaultdict, deque

INPUT_FILE = "input"


def solve():
    rules = {}
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()

        for line in lines:
            s = line.strip().split(" bags contain ")

            content = defaultdict(int)
            for comp in s[1].split(", "):
                words = comp.split(" ")
                if words[0] != "no":
                    content[words[1] + " " + words[2]] = int(words[0])
            rules[s[0]] = content

        bags = set(["shiny gold"])
        l = 0
        while len(bags) > l:
            l = len(bags)
            for key in rules:
                if any(color in rules[key] for color in bags):
                    bags.add(key)

        bags2 = defaultdict(int)
        q = deque([("shiny gold", 1)])

        while len(q) > 0:
            color, amount = q.pop()

            for key in rules[color]:
                q.append((key, rules[color][key] * amount))
                bags2[key] += rules[color][key] * amount

        return len(bags) - 1, sum(bags2.values())


if __name__ == "__main__":
    part1, part2 = solve()
    print(part1)
    print(part2)
