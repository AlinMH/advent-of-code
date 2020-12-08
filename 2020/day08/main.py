from copy import deepcopy

INPUT_FILE = "input"


def part1():
    acc = 0
    ip = 0
    sequence = set()

    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()

        while ip not in sequence:
            sequence.add(ip)
            if lines[ip].startswith("acc"):
                acc += int(lines[ip][3:])
                ip += 1
            elif lines[ip].startswith("jmp"):
                ip += int(lines[ip][3:])
            elif lines[ip].startswith("nop"):
                ip += 1

        return acc


def part2():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()
        nops = [idx for idx, val in enumerate(lines) if val.startswith("nop")]
        jmps = [idx for idx, val in enumerate(lines) if val.startswith("jmp")]

        while True:
            for instr in nops + jmps:
                _lines = deepcopy(lines)
                ip = 0
                acc = 0
                sequence = set()

                if _lines[instr].startswith("nop"):
                    _lines[instr] = _lines[instr].replace("nop", "jmp")
                else:
                    _lines[instr] = _lines[instr].replace("jmp", "nop")

                while ip not in sequence:
                    if ip >= len(_lines):
                        return acc

                    sequence.add(ip)
                    if _lines[ip].startswith("acc"):
                        acc += int(_lines[ip][3:])
                        ip += 1
                    elif _lines[ip].startswith("jmp"):
                        ip += int(_lines[ip][3:])
                    elif _lines[ip].startswith("nop"):
                        ip += 1


if __name__ == "__main__":
    part1 = part1()
    print(part1)

    part2 = part2()
    print(part2)
