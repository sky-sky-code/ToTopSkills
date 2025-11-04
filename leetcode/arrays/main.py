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


def removeDuplicates(nums):
    if not nums:
        return 0

    # Two-pointer approach
    k = 1  # Position for next unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


def maxProfit(prices) -> int:
    current_max_profit = 0
    index_current_price = 0

    for i in range(1, len(prices)):
        next_price = prices[i]
        if prices[index_current_price] < next_price:
            current_max_profit = current_max_profit + (next_price - prices[index_current_price])
        index_current_price = i
    return current_max_profit