import os
from copy import deepcopy
import math as m
from math import prod

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        et, bus_ids = fp.read().splitlines()
        et = int(et)
        bus_ids = bus_ids.split(",")
        bus_ids = list(map(int, filter(lambda x: x != "x", bus_ids)))
        min_time, id = min(map(lambda x: (x - et % x, x), bus_ids), key=lambda x: x[0])
        return min_time * id


def part2():
    with open(INPUT_FILE, "r") as fp:
        _, bus_ids = fp.read().splitlines()
        bus_ids = bus_ids.split(",")
        bus_ids = [(int(val), int(val) - id) for id, val in enumerate(bus_ids) if val != "x"]
        return chinese_remainder([x[0] for x in bus_ids], [x[1] for x in bus_ids])

        
def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


if __name__ == "__main__":
    result = part1()
    print(result)

    result = part2()
    print(result)
