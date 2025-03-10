#################################################################
from collections import defaultdict


def mul(arr):
    x_mul = arr[0]
    for i in arr[1:]:
        x_mul *= i
    return x_mul


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


print(three_sum([-1, 0, 1, 2, -1, -4]))


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:

        total = nums[left] + nums[right]

        if total == target:
            if total == 0:
                return []
            return [left + 1, right + 1]

        if total > target:
            right -= 1
        else:
            left += 1


def rotate_arr(nums, k):
    for i in range(k):
        rotate_num = nums.pop(-1)
        nums.insert(0, rotate_num)
    return nums


def rotate_arr_v2(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


def rotate_arr_v3(nums, k):
    k = k & len(nums)

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


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


def max_profit_ex(prices):
    min_price = float('inf')
    max_profit = -float('inf')

    for i in prices:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)

    return max_profit


def max_profit_dp(prices):
    dp = [0] * len(prices)
    min_price = prices[0]

    for p in range(1, len(prices)):
        min_price = min(min_price, prices[p])
        dp[p] = max(dp[p - 1], prices[p] - min_price)

    return dp[-1]


def product_except_self(nums):
    prefix = nums[:1] + ([0] * (len(nums) - 1))

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * i

    suffix = 1
    for i in range(len(nums) - 2, -1, -1):
        suffix *= nums[i + 1]
        prefix[i] *= suffix

    print(prefix)
    return prefix


def longest_palindromic_substrings(s):
    longest = ""

    for i in range(len(s)):
        for left, right in [(i, i), (i, i + 1)]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(longest) < right - left - 1:
                longest = s[left + 1:right]

    print(longest)
    return longest


def max_area(nums):
    left, right = 0, len(nums) - 1

    ans = 0
    while left <= right:
        ans = max(ans, (right - left) * min(nums[left], nums[right]))

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    print(ans)
    return ans


def minimaze_subarray_sum(nums, target):
    left = 0
    prefix = 0
    right = 0
    ans = float('inf')

    while True:
        if prefix >= target:
            left += 1
            prefix -= nums[left]
            print(prefix)
            ans = min(ans, right - left + 1)
        else:
            right += 1
            if right >= len(nums):
                break
            prefix += nums[right]

    return ans if ans != float('inf') else 0


def longest_substring_without_repeat(s):
    n = len(s)
    maxLength = 0
    charMap = {}
    left = 0

    for right in range(n):
        if s[right] not in charMap or charMap[s[right]] < left:
            charMap[s[right]] = right
            maxLength = max(maxLength, right - left + 1)
        else:
            left = charMap[s[right]] + 1
            charMap[s[right]] = right

    return maxLength


"""
Учитывая массив intervals где intervals[i] = [starti, endi], объедините все перекрывающиеся интервалы
и верните массив неперекрывающихся интервалов, которые охватывают все интервалы во входных данных.
"""


def merge_intervals(intervals):
    intervals = sorted(intervals)
    result = []

    for interval in intervals:
        if len(result) == 0:
            result.append(interval)
        else:
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
    return result


def insert_interval(intervals, new_interval):
    result = []
    for i, interval in enumerate(intervals):
        if new_interval[0] > interval[1]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            return result + [new_interval] + intervals[i:]
        else:
            new_interval = (min(new_interval[0], interval[0]), max(new_interval[1], interval[1]))

    return result + [new_interval]


def find_min_intervals(intervals):
    """
    [[1, 6], [2, 8], [7, 12], [10, 16]]
   [[0, 6], [0, 9], [2, 8], [2, 9], [3, 8], [3, 9], [3, 9], [6, 8], [7, 12], [9, 10]]
    """
    intervals.sort(key=lambda x: x[1])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if result[-1][1] < interval[0]:
            result.append(interval)

    return len(result)


from math import ceil

# def maxk_elements(nums, k):
#     nums.sort()
#     right = len(nums) - 1
#     sum = 0
#
#     while k and 0 <= right:
#         if nums[right - 1] > nums[right]:
#             right -= 1
#         else:
#             sum += nums[right]
#             nums[right] = ceil(nums[right] / k)
#             k -= 1
#
#     return sum

import heapq


def maxk_elements(nums, k):
    nums.sort()
    result = 0

    while k > 0:
        k -= 1
        nums.sort()
        max_element = nums.pop(len(nums) - 1)
        result += max_element
        nums.append(ceil(max_element / 3))
    return result


def maxKelements(nums, k) -> int:
    ans = 0
    max_heap = []

    # Add elements one by one into the max-heap
    for num in nums:
        heapq.heappush(max_heap, -num)

    while k > 0:
        k -= 1
        # Retrieve the max element (invert the sign because it's stored as negative)
        max_element = -heapq.heappop(max_heap)
        ans += max_element
        # Add one-third of the max element back to the heap. Rounded up using integer division.
        heapq.heappush(max_heap, -ceil(max_element / 3))

    return ans


print(maxk_elements([756902131,995414896,95906472,149914376,387433380,848985151], 6 ))
