INPUT_FILE = "PATH_TO_INPUT"

def part_1():
    valid_passwords = 0
    with open(INPUT_FILE, "r") as fp:
        for line in fp:
            line_split = line.split(": ")
            password_policy = line_split[0]
            password = line_split[1]

            pp_split = password_policy.split(" ") 
            boundary = pp_split[0]
            char = pp_split[1]

            boundary_split = boundary.split("-")
            low = int(boundary_split[0])
            high = int(boundary_split[1])
            
            if low <= password.count(char) <= high:
                valid_passwords += 1
    
    return valid_passwords

def part_2():
    valid_passwords = 0
    with open(INPUT_FILE, "r") as fp:
        for line in fp:
            line_split = line.split(": ")
            password_policy = line_split[0]
            password = line_split[1]

            pp_split = password_policy.split(" ") 
            boundary = pp_split[0]
            char = pp_split[1]

            boundary_split = boundary.split("-")
            low = int(boundary_split[0])
            high = int(boundary_split[1])
            if (password[low - 1] == char) ^ (password[high - 1] == char):
                valid_passwords += 1
    
    return valid_passwords

if __name__ == "__main__":
    result = part_1()
    print(result)
    result = part_2()
    print(result)