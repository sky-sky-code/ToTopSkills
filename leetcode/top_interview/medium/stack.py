def isValid(brackets):
    stack = []
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for bracket in brackets:
        if bracket.startswith(('(', '[', '{')):
            stack.append(bracket)
        elif not stack and bracket.startswith((')', ']', '}')):
            return False
        elif bracket_map[bracket] != stack.pop(-1):
            return False
    return True if not stack else False


print(isValid("([{}])"))


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


def simplify_path(path):
    path = path.split('/')
    output = []

    for catalog in path:
        if catalog == '' or catalog == ".":
            continue
        elif catalog == '..':
            if output:
                output.pop(-1)
        else:
            output.append(catalog)
    path = '/'.join(output)

    return '/' + path


def eval_RPN_v1(tokens):
    result = None
    index = 0
    while index <= len(tokens) - 1:
        if tokens[index].startswith(('+', '-', '*', '/')):
            if result is None:
                opert = tokens.pop(index)
                index -= 1
                first_num = tokens.pop(index)
                index -= 1
                two_num = tokens.pop(index)
                result = eval(f'{two_num}{opert}{first_num}')
            else:
                opert = tokens.pop(index)
                index -= 1
                two_num = tokens.pop(index)
                index -= 1
                result = eval(f'{two_num}{opert}{result}')
        index += 1
    if tokens:
        opert = tokens.pop(-1)
        num = tokens.pop(-1)
        result = eval(f'{num}{opert}{result}')
    print(int(result))
    return int(result)


def eval_RPM(tokens):
    stack = []
    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            second, first = stack.pop(), stack.pop()
            stack.append(first - second)
        elif c == '/':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first / second))
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(c))
    return stack[0]
