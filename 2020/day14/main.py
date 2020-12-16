import itertools
import os
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        mem = {}

        for line in lines:
            lhs, rhs = line.split(" = ")

            if lhs == "mask":
                mask = rhs

            else:
                mem_addr = int(lhs[4:-1])
                val = int(rhs)
                or_mask = int(mask.replace("X", "0"), base=2)
                and_mask = int(mask.replace("X", "1"), base=2)
                mem[mem_addr] = (val | or_mask) & and_mask

        return sum(mem.values())


def part2():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()

        mem = {}
        mask_to_1 = 0
        float_positions = []

        for line in lines:
            lhs, rhs = line.split(" = ")

            if lhs == "mask":
                mask = rhs
                mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
                float_positions = [i for i, x in enumerate(reversed(mask)) if x == "X"]
            else:
                address, value = (int(x) for x in re.findall(r"(\d+)", line))
                address = address | mask_to_1
                for bits in itertools.product((0, 1), repeat=len(float_positions)):
                    mask_toggle = 0
                    for b, i in zip(bits, float_positions):
                        mask_toggle = mask_toggle ^ (b << i)
                    mem[address ^ mask_toggle] = value

        return sum(mem.values())


if __name__ == "__main__":
    result = part1()
    print(result)

    result = part2()
    print(result)
