"""
Данный фацл черновик для записей
и закрепления материала путем перерешиванием задач снова и снова
"""


def merge(nums1, m, nums2, n):
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    return nums1


def remove_element(nums, val):
    index = 0
    while nums and nums[index] != '_':
        if nums[index] == val:
            nums.pop(index)
            nums.append('_')
            continue
        index += 1
        if index == len(nums):
            break

    return index


def remove_duplicates(nums):
    current_nums = nums[0]
    index = 1
    while index <= len(nums) - 1 and nums[index] != '_':
        if nums[index] == current_nums:
            nums.pop(index)
        else:
            current_nums = nums[index]
            index += 1
    return len(nums)


def remove_duplicates_v2(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j - 1]:
            nums[i] = nums[j]
            i += 1

    return i


def remove_duplicates_2(nums):
    current_nums = nums[0]
    count_num = 1

    index = 1
    while index <= len(nums) - 1:
        if nums[index] == current_nums:
            count_num += 1
            if count_num > 2:
                nums.pop(index)
                count_num -= 1
                continue
        else:
            current_nums = nums[index]
            count_num = 1
        index += 1
    return len(nums)


"""
еще раз решить majority element, jump_game, Best Time to Buy and Sell Stock
"""


def majority_element(nums):
    current_num = nums[0]
    count = 1

    for num in nums:
        if num == current_num:
            count += 1
        else:
            if count < 0:
                current_num = num
                count = 1
            count -= 1
    return current_num


def is_palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True


def is_palindrome_v2(s):
    s = ''.join([word for word in s if word.isalnum()])
    new_s = s[::-1]

    if s.lower() == new_s.lower():
        return True
    else:
        return False


def is_subsequence(s, t):
    point = 0
    new_s = ''

    for word in t:
        if s[point] == word:
            new_s += word
            point += 1
            if point >= len(s):
                break
    if s == new_s:
        return True
    else:
        return False



