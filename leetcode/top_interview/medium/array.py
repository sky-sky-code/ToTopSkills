#################################################################
from collections import defaultdict


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

def three_sum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res


def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


# Group Anagram
def group_anagram(arr):
    result = []


def jump_game(arr):
    gas = 0

    for i in arr:
        if gas < 0:
            return False
        elif gas < i:
            gas = i
        gas -= 1
    return True


def jump_game_2(nums):
    ans = end = far = 0

    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if far >= len(nums):
            ans += 1
            break
        if i == end:
            ans += 1
            end = far
    return ans


def jump_game_v2(nums):
    near = far = jump = 0

    while far <= len(nums):
        farthest = 0
        for i in range(near, far + 1):
            farthest = max(far, i + nums[i])
        near = far + 1
        far = farthest
        jump += 1
    return jump


def h_index(nums):
    nums.sort(reverse=True)
    h = 0
    for i in range(len(nums)):
        if nums[i] >= i + 1:
            h += 1
        else:
            break
    return h


def product_except_self(arr):
    suf = [1] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        suf[i] = suf[i + 1] * arr[i + 1]

    prefix = 1
    for i in range(1, len(arr)):
        prefix *= arr[i - 1]
        suf[i] *= prefix
    return suf

