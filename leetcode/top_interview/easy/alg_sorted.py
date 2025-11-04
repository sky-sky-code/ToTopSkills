def isbadversion(bad):
    dct = {
        1: False,
        2: False,
        3: False,
        4: True,
        5: True,
    }
    return dct[bad]


def first_bad_version(n, bad):
    left, right = 1, n
    mid = (left + right) // 2

    while right - left != 1:
        mid = (left + right) // 2
        if not isbadversion(mid):
            left = mid
        else:
            right = mid

    return mid


def merge_sorted_array(nums1, m, nums2, n):
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


# Quicksort

def quicksort(nums):
    if len(nums) < 2:
        return nums

    pivot = nums[0]

    less = [i for i in nums[1:] if i < pivot]
    more = [i for i in nums[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(more)


def buble_sort(nums):
    for index in range(len(nums) - 1):
        for jndex in range(len(nums) - 1 - index):
            if nums[jndex] > nums[jndex + 1]:
                nums[jndex], nums[jndex + 1] = nums[jndex + 1], nums[jndex]
    return nums
