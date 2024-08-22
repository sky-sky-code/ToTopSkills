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
