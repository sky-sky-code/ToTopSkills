"""
 Дан отсортированный масисв [-5, -4, -3, 1, 2, 4, 5]
 возвести числа в квадрат и вывести в отсортированном ввиде

"""
import collections


def solution(arr):
    right = len(arr) - 1
    left = 0
    result = []
    while left <= right:
        if abs(arr[left]) > arr[right]:
            result.append(arr[left] ** 2)
            left += 1
        else:
            result.append(arr[right] ** 2)
            right -= 1
    return result[::-1]


"""
Дан массив nums = [6, 1, 3, 7, 0, 1]
k = 3 вывести максимальный элемент равный окну k
"""


def solution_v2(arr, k):
    left, window = 0, k

    result = []
    while window <= len(arr):
        max_current_num = arr[left]
        for i in arr[left + 1:window]:
            if max_current_num < i:
                max_current_num = i
        result.append(max_current_num)
        left, window = left + 1, window + 1
    return result


"""
На вход приходит массив не сортированый из него удалили элемента надо его найти
"""


def solution_v3(arr):
    len_arr = len(arr)
    real_arr = len_arr + 1

    s = real_arr * (real_arr + 1) / 2
    return s - sum(arr)


"""
Merge Intervals
[1, 2, 3, 4, 6, 8, 9] => "1-4,6,8-9"
"""


def solution_v4(nums):
    nums = sorted(nums)

    index = 0
    offset = 0
    new_arr = []
    while index <= len(nums) - 1:
        next_index = index + 1
        if next_index > len(nums) - 1:
            if offset == index:
                new_arr.append(f'{nums[offset]}')
                break
            new_arr.append(f'{nums[offset]}-{nums[index]}')
            break
        if nums[index] + 1 != nums[next_index]:
            if index == offset:
                new_arr.append(f'{nums[offset]}')
                index += 1
                offset = index
                continue
            new_arr.append(f'{nums[offset]}-{nums[index]}')
            offset = index + 1
        index += 1
    return ','.join(new_arr)


"""
Summary Ranges одно и тоже задание с Merge Intervals
"""


def summary_ranges(nums):
    set_nums = set(nums)
    intervals = []

    for num in nums:
        if num - 1 not in set_nums:
            len = 1
            interval = f"{num}->"
            while num + len in set_nums:
                len += 1
            if num + len - 1 == num:
                interval = f"{num}"
            else:
                interval += f"{num + len - 1}"
            intervals.append(interval)
    return intervals


print(summary_ranges([0, 1, 2, 4, 5, 7]))


# Plus One

def plus_one(arr):
    s = int(''.join([str(i) for i in arr])) + 1
    return [int(i) for i in str(s)]


# Moves Zero

def move_zero(arr):
    index, counter = 0, 0
    while counter < len(arr):
        if arr[index] == 0:
            arr.append(arr.pop(index))
        else:
            index += 1
        counter += 1
    return arr


# Remove Duplicates from Sorted Array

def remove_duplicates():
    arr = [int(i) for i in input().split(' ')]
    index = 0
    while arr[index] != '_':
        if arr[index] == arr[index + 1]:
            arr.pop(index)
            arr.append('_')
        else:
            index += 1

    print(arr)


def remove_duplicates_v2(nums):
    k = 0
    index = 0
    while nums[index] != '_':
        if nums[index + 1] == nums[index]:
            nums.pop(index + 1)
            nums.append('_')
            k += 1
        else:
            index += 1
    return k, nums


# Rotate Array

def rotate_array_v1(arr):
    rotate = int(input()) * -1
    return arr[rotate:] + arr[:rotate]


def rotate_array_v2(arr):
    rotate = int(input())

    for i in range(1, rotate + 1):
        el = arr.pop(-1)
        arr.insert(0, el)
    print(arr)


# Contains Duplicate

def contains_element(nums: list):
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False


# Rotate Image

def rotate_image(matrix):
    pass


# Valid Sudoku

def valid_sudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            # if it's empty skip it
            if board[r][c] == ".":
                continue
            # have we found a duplicate
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False
            # if it is valid
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
        # if we never detect duplicates
    return True


def majority_element(nums):
    """
    Алгоритм Бойера - Мура
    """

    candidate = nums[0]
    count = 1
    for i in nums:
        if i == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = i
                count = 1
    return candidate
