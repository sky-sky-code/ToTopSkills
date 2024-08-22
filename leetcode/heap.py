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
    count_nums = 1

    index = 1
    while index < len(nums) - 1:
        if nums[index] != current_nums:
            current_nums = nums[index]
            count_nums = 1
        elif count_nums > 2:
            nums.pop(index)
        else:
            count_nums += 1


