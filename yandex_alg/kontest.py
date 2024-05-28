def stones_and_jewerly(j, s):
    current_check_position = len(j)
    start_stone = 0

    result = 0
    while current_check_position <= len(s):
        if s[start_stone:current_check_position] == j:
            result += 1
        start_stone += 1
        current_check_position += 1
    return result


def stones_and_jewerly_v2(j, s):
    """
    abacg

    ab,  ba, cg

    """
    for index in range(len(s) - 1):
        if s[index:index + len(j)] == j:
            return s[index:index + len(j)]


def stones_and_jewerly_v3(j, s):
    result = 0
    for i in s:
        if i in j:
            result += 1
    return result


def seq_point():
    n = int(input())
    flag_stop = 0

    current_max_seq = 0
    counter = 0
    while flag_stop != n:
        point = int(input())
        if point == 1:
            counter += 1
        else:
            current_max_seq = counter
            counter = 0
        flag_stop += 1
    return current_max_seq


def stack_brackets():
    n = int(input())
    stack = [None] * n * 2
    index = 0
    while index != len(stack) // 2:
        stack[index], stack[(index + 1) * -1] = '(', ')'
        index += 1
    return stack


def bracket(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            bracket(count, s + '(', left + 1, right)
        if right < left:
            bracket(count, s + ')', left, right + 1)

