# Reverse STRING

def reverse_str(string):
    start_index = 0
    end_index = len(string) - 1

    while start_index <= end_index:
        string[start_index], string[end_index] = string[end_index], string[start_index]
        start_index += 1
        end_index -= 1
    return ''.join(string)


# Reverse Integer

def reverse_int(x):
    negative_or_not = -1 if x < 0 else 1
    result = int(str(abs(x))[::-1]) * negative_or_not
    if result > 2 ** 31 or result < 2 ** 31 * -1:
        return 0
    return result


# First Unique Character in a String

def first_character(s):
    s = list(s)
    counter = {}
    for i in s:
        counter[i] = counter.get(i, 0) + 1

    for index in range(len(s)):
        if counter[s[index]] == 1:
            return index
    return -1


# Valid Anagram

def is_anagram(s, t):
    counter_s = {}
    for i in s:
        counter_s[i] = counter_s.get(i, 0) + 1
    counter_t = {}
    for i in t:
        counter_t[i] = counter_t.get(i, 0) + 1
    return counter_s == counter_t


# Valid Palindrome

def is_polindrome(s: str):
    s = s.replace(' ', '').replace(',', '').replace(':', '').replace('.', '')
    iters = len(s) // 2
    for i in range(iters):
        if s[i].lower() != s[-i - 1].lower():
            return False
    return True


# Implement strStr

def implement_str(haystack, needle):
    step_needle = len(needle)
    for index in range(len(haystack)):
        if step_needle > len(haystack):
            break
        if haystack[index:step_needle] == needle:
            return index
        step_needle += 1
    return -1


# Longest Common Prefix

def common_prefix(strs):
    shortest = min(strs, key=len)
    index_prefix = 0
    support_str = strs.pop(0)
    while index_prefix <= len(shortest):
        for s in strs:
            if support_str[:index_prefix + 1] != s[:index_prefix + 1]:
                return support_str[:index_prefix] if index_prefix != 0 else ""
        index_prefix += 1


# Seq  brackets_check
def brackets_check(seq):
    stack = []
    for i in range(len(seq)):
        if seq[i] == '(':
            stack.append('(')
        else:
            if seq[i] == stack.pop():
                return False
    return True


def len_last_word(s):
    length = 0
    flag = False
    for i in range(len(s) - 1, 0, -1):
        if s[i] != ' ':
            flag = True
            length += 1
        elif flag:
            break
    return length


def reverse_words(s):
    s = s.strip()
    index = len(s) - 1

    result = ''
    while index >= 0:
        if s[index] == ' ':
            result += f'{s[index + 1:]} '
            s = s[:index].strip()
            index = len(s) - 1
        index -= 1

    return result + s

