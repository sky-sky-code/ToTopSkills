#################################################################
import sys
from collections import defaultdict
from typing import List


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
    return longest

print(longest_palindromic_substrings('babad'))


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

longest_substring_without_repeat('abcabcbb')


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


def threeSumCloset(nums, target):
    nums = sorted(nums)
    min_result = float('inf')
    max_result = float('-inf')

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total < target:
                min_result = min(min_result, total)
                j += 1
            elif total > target:
                max_result = max(max_result, total)
                k -= 1
            else:
                return total
    return


def search(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return target
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def search_range(n: List[int], t: int) -> int:
    left = 0
    right = len(n) - 1

    start, end = -1, -1
    while left <= right:
        mid = (left + right) // 2

        if n[mid] == t:
            start = mid
            end = mid
            while start > 0 and n[start - 1] == t:
                start = start - 1
            while end < len(n) - 1 and n[end + 1] == t:
                end = end + 1
            break
        elif n[mid] > t:
            right = mid - 1
        elif n[mid] < t:
            left = mid + 1

    return [start, end]


def find_max_product(A):
    max1 = A[0]
    max2 = -sys.maxsize

    min1 = A[0]
    min2 = sys.maxsize

    for i in range(1, len(A)):
        if A[i] > max1:
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            max2 = A[i]

        if A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]


#TODO решить еще раз
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    pass


def jump_2(nums):
    last = farthest = jump = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == last:
            last = farthest
            jump += 1
    return jump


#TODO решите еще раз
def permute(nums: List[int]) -> List[List[int]]:
    pass


def subsets(nums: List[int]) -> List[List[int]]:
    pass
