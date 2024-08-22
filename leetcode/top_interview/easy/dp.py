"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
from typing import List


def climb_stairs(n):
    one, two = 1, 1
    # since we initialized one,two, we have to compute only n-1 values. remember n-1 is not inclusive
    for i in range(n - 1):
        one, two = two, one + two
    return two


def maxProfit(prices):
    n = len(prices)
    buy = prices[0]
    max_profit = 0
    for i in range(1, n):

        # Checking for lower buy value
        if (buy > prices[i]):
            buy = prices[i]

        # Checking for higher profit
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit


def max_subarray(nums: List[int]) -> int:
    head_index = 0
    current_sum = sum(nums)
    for index in range(1, len(nums)):
        if sum(nums[index:]) > current_sum:
            head_index = index
            current_sum = sum(nums[index:])

    if len(nums) - 1 == head_index:
        return sum(nums[head_index:])

    tail_index = nums[-1]
    for index in range(len(nums) - 1, head_index, -1):
        if sum(nums[head_index:index]) > current_sum:
            current_sum = sum(nums[head_index:index])
            tail_index = index

    return sum(nums[head_index:tail_index])


def max_subarray_v2(nums: List[int]) -> int:
    max_so_far = float("-inf")
    max_ending_here = 0

    for i in range(0, len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def max_subarray_dp_v3(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    ans = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])

        ans = max(ans, dp[i])

    return ans


def house_robber(nums: List[int]) -> int:
    """
    [1,2,3,1]
    dp[0] = 1
    dp[1] = 2
    """
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]
