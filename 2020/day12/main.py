import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def part1():
    with open(INPUT_FILE, "r") as fp:
        instructions = fp.read().splitlines()

        dir = 1  # East
        x, y = 0, 0

        for instr in instructions:
            command = instr[0]
            arg = int(instr[1:])

            if command == "F":
                if dir == 1:
                    x += arg
                elif dir == 3:
                    x -= arg
                elif dir == 0:
                    y += arg
                elif dir == 2:
                    y -= arg

            elif command == "E":
                x += arg
            elif command == "W":
                x -= arg
            elif command == "N":
                y += arg
            elif command == "S":
                y -= arg

            elif command == "R":
                dir = (dir + int(arg / 90)) % 4
            elif command == "L":
                dir = (dir - int(arg / 90)) % 4

        return abs(x) + abs(y)


def part2():
    with open(INPUT_FILE, "r") as fp:
        instructions = fp.read().splitlines()
        pos = 0 + 0j
        waypoint = 1 + 10j

        for instr in instructions:
            command = instr[0]
            arg = int(instr[1:])
            if command == "N":
                waypoint += arg

            elif command == "S":
                waypoint -= arg

            elif command == "E":
                waypoint += 1j * arg

            elif command == "W":
                waypoint -= 1j * arg

            elif command == "F":
                pos += waypoint * arg
            
            elif command == "R":
                while arg > 0:
                    waypoint *= 1j
                    arg -= 90
            
            elif command == "L":
                while arg > 0:
                    waypoint *= -1j
                    arg -= 90

        return int(abs(pos.real) + abs(pos.imag))

if __name__ == "__main__":
    result = part1()
    print(result)

    result = part2()
    print(result)
