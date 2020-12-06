from functools import reduce

INPUT_FILE = "/home/alin_ubuntu/alin/python_stuff/advent-of-code/2020/day6/input"

def part_1():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()

        counter = 0
        current_answers = set()
        for line in lines:
            if line == "\n":
                counter += len(current_answers) 
                current_answers.clear()
            else:
                current_answers.update(set(line[:-1]))

        return counter

def part_2():
    with open(INPUT_FILE, "r") as fp:
        lines = fp.readlines()

        counter = 0
        current_answers = []
        for line in lines:
            if line == "\n":
                counter += len(reduce(lambda x, y: x.intersection(y), current_answers)) 
                current_answers.clear()
            else:
                current_answers.append(set(line[:-1]))

        return counter

if __name__ == "__main__":
    result = part_1()
    print(result)

    result = part_2()
    print(result)

