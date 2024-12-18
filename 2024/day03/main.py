import re


def part1(to_parse: str):
    res_sum = 0
    res = re.findall(r"mul\(\d{1,3},\d{1,3}\)", to_parse)
    for i in res:
        num1, num2 = i.replace("mul(", "").replace(")", "").split(",")
        res_sum += int(num1) * int(num2)

    print(res_sum)


def part2(to_parse: str):
    do = 1
    res_sum = 0
    res = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", to_parse)

    for i in res:
        if i == "do()":
            do = 1
            continue

        if i == "don't()":
            do = 0
            continue

        if do == 1:
            num1, num2 = i.replace("mul(", "").replace(")", "").split(",")
            res_sum += int(num1) * int(num2)

    print(res_sum)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        line = "".join(lines)
        part2(line)
