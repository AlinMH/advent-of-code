import os
from copy import deepcopy
import math as m

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
        


if __name__ == "__main__":
    result = part1()
    print(result)

    result = part2()
    print(result)
