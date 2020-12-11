import re
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")

eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

BYR = "byr"
IYR = "iyr"
EYR = "eyr"
HGT = "hgt"
HCL = "hcl"
ECL = "ecl"
PID = "pid"

required_fields = {BYR, IYR, EYR, HGT, HCL, ECL, PID}


def part_1():
    valid = 0
    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()

        curr_fields = set()
        for line in lines:
            if line == "\n":
                if curr_fields.intersection(required_fields) == required_fields:
                    valid += 1
                curr_fields.clear()
            else:
                curr_fields.update(set(re.split(":| ", line)[::2]))

    return valid


def part_2():
    valid = 0
    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()

        curr_fields = {}
        for line in lines:
            if line == "\n":
                if is_valid(curr_fields):
                    valid += 1
                curr_fields.clear()
            else:
                kv_list = re.split(":| ", line[:-1])
                zipped_list = zip(kv_list[::2], kv_list[1::2])
                curr_fields.update(dict(zipped_list))
    return valid


def is_valid(curr_fields):
    if not set(curr_fields.keys()).intersection(required_fields) == required_fields:
        return False

    try:
        if not 1920 <= int(curr_fields[BYR]) <= 2002:
            return False

        if not 2010 <= int(curr_fields[IYR]) <= 2020:
            return False

        if not 2020 <= int(curr_fields[EYR]) <= 2030:
            return False

        hgt = curr_fields[HGT]
        if hgt[-2:] == "in":
            if not 59 <= int(hgt[:-2]) <= 76:
                return False
        elif hgt[-2:] == "cm":
            if not 150 <= int(hgt[:-2]) <= 193:
                return False
        else:
            return False

        if not re.match("#([0-9]|[a-f]){6}", curr_fields[HCL]):
            return False

        if not curr_fields[ECL] in eye_colors:
            return False

        pid = curr_fields[PID]
        if not (len(pid) == 9 and pid.isdigit()):
            return False

        return True

    except Exception as e:
        print(repr(e))
        return False


if __name__ == "__main__":
    result = part_1()
    print(result)

    result = part_2()
    print(result)
