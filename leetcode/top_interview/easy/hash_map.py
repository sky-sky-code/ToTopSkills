from collections import defaultdict

"""
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""
from collections import Counter


def ransom_note(ransom_note, magazine):
    counter = Counter(magazine)

    for word in ransom_note:
        if word not in counter.keys():
            return False
        if counter[word] == 0:
            return False
        counter[word] = counter[word] - 1

    return True


"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""


def isomorphic_strings(s, t):
    dct = {}
    set_vals = set()
    for i in range(len(s)):
        if s[i] not in dct.keys():
            if t[i] in set_vals:
                return False
            dct[s[i]] = t[i]
            set_vals.add(t[i])
        else:
            if dct[s[i]] != t[i]:
                return False
    return True


"""
Given a pattern and a string s, find if s follows the same pattern. pattern and s are same if:
each character in pattern represents a word in s
No two distinct characters in pattern can represent the same word in s
No single character in pattern can represent two distinct words in s.
"""


def word_pattern(pattern, s):
    dct = {}
    word_set = set()

    split_s = s.split(' ')
    if len(split_s) != len(pattern):
        return False

    for i in range(len(split_s)):
        if pattern[i] not in dct.keys():
            if split_s[i] in word_set:
                return False
            dct[pattern[i]] = split_s[i]
            word_set.add(split_s[i])
        else:
            if dct[pattern[i]] != split_s[i]:
                return False
    return True


def two_sum(nums, target):
    dct = {}
    for index, num in enumerate(nums):
        if num in dct.keys():
            return [dct[num], index]
        dct[target - num] = index
