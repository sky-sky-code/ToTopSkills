
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
from collections import defaultdict


def longest_consecutive_seq(nums):
    set_nums = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in set_nums:
            len = 1
            while num + len in set_nums:
                len += 1
            longest = max(longest, len)
    return longest


"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


def group_anagrams(strs):
    dct = defaultdict(list)

    for i in strs:
        key = ''.join(sorted(i))
        dct[key].append(i)
    return dct.values()
