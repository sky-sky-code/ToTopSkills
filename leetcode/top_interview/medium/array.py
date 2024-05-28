#################################################################
def mul(arr):
    x_mul = arr[0]
    for i in arr[1:]:
        x_mul *= i
    return x_mul


def product_except_self(arr):
    result = []
    index = 0
    while index < len(arr):
        self = arr.pop(index)
        product_self = mul(arr)
        result.append(product_self)
        arr.insert(index, self)
        index += 1

    return result


##################################################################

def product_except_self_v2(arr):
    ans = [1]

    for index in range(1, len(arr)):
        ans.append(ans[-1] * arr[index - 1])

    cur = 1
    for index in range(len(arr) - 2, -1, -1):
        cur *= arr[index + 1]
        ans[index] *= cur
    return ans


# 3 Sum

def three_sum(arr):
    current_num = arr.pop(0)

    start_check = 0
    finish_check = 2

    result = []
    while len(arr) >= 2:
        if current_num + sum(arr[start_check:finish_check]) == 0:
            result.append([current_num] + arr[start_check:finish_check])
            del arr[start_check:finish_check]
            start_check, finish_check = 0, 2
        else:
            start_check += finish_check
            finish_check += 2
    return result


# Group Anagram
def group_anagram(arr):
    result = []
