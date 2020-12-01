INPUT_FILE = "PATH_TO_INPUT"

def solve():
    with open(INPUT_FILE, "r") as fp:
        s = set(map(lambda x: int(x), fp))
        
        for elem in s:
            if 2020 - elem in s:
                return elem * (2020 - elem)

if __name__ == "__main__":
    result = solve()
    print(result)
