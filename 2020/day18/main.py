import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input")


def get_precedence(op, part1=True):
    if part1:
        return 0

    return 0 if op == "*" else 1


def evaluate(expression: str, part1=True):
    expression = expression.replace("(", "( ").replace(")", " )").split(" ")
    ops = []
    vals = []

    for c in expression:
        if c == "(":
            ops.append(c)

        elif c.isdigit():
            vals.append(int(c))

        elif c == ")":
            while ops and ops[-1] != "(":
                compute_val(ops, vals)

            ops.pop()

        else:
            while ops and ops[-1] != "(" and get_precedence(ops[-1], part1) >= get_precedence(c, part1):
                compute_val(ops, vals)

            ops.append(c)

    while ops:
        compute_val(ops, vals)

    return vals[-1]


def compute_val(ops, vals):
    lhs = vals.pop()
    rhs = vals.pop()
    op = ops.pop()
    vals.append(calc(lhs, rhs, op))


def calc(lhs, rhs, op):
    return rhs + lhs if op == "+" else rhs * lhs


def solve(part1=True):
    with open(INPUT_FILE, "r") as fp:
        lines = fp.read().splitlines()

        return sum(map(lambda x: evaluate(x, part1=part1), lines))


if __name__ == "__main__":
    result = solve()
    print(result)

    result = solve(part1=False)
    print(result)
