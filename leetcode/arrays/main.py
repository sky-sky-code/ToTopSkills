# Max Consecutive Ones

"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""


def max_consecutive(nums):
    count_ones = 0
    max_count = 0
    for num in nums:
        if num == 0:
            if count_ones >= max_count:
                max_count = count_ones
            count_ones = 0
            continue
        count_ones += 1
    return max_count if max_count > count_ones else count_ones


"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


def sqrt_sorted(nums):
    pass


"""
Duplicate Zero
"""


def duplicate_zeroes(arr):
    index = 0
    fix_len = len(arr) - 1

    while index <= fix_len:
        if arr[index] == 0:
            arr.insert(index, 0)
            index += 2
            arr.pop()
        else:
            index += 1
    return arr


print(duplicate_zeroes([1, 2, 3]))
