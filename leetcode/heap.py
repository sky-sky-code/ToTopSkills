"""
Данный файл черновик для записей
и закрепления материала путем перерешиванием задач снова и снова
"""

from typing import List


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


def jump_game_2(nums):
    last = maax = jump = 0

    for i in range(len(nums) - 1):
        maax = max(maax, i + nums[i])

        if i == last:
            last = maax
            jump += 1

    return jump


def longest_common_prefix(strs):
    min_str = min(strs)
    current_index = 0
    while current_index <= len(min_str) - 1:
        for str in strs:
            if min_str[:current_index + 1] != str[:current_index + 1]:
                return '' if current_index == 0 else min_str[:current_index]
        current_index += 1
    return min_str


def longest_common_prefix_v2(strs):
    """
    ЗБС решение
    """


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


def hasystack_needle(haystack, needle):
    two_pointer = len(needle)

    for i in range(len(haystack)):
        if haystack[i:two_pointer] != needle:
            two_pointer += 1
        else:
            return i
    return -1


def two_sum(nums, target):
    first = 0
    second = 1

    while first <= len(nums) - 1 and second <= len(nums) - 1:
        total = target - nums[first]
        while second <= len(nums) - 1:
            if nums[second] == total:
                return first + 1, second + 1
            second += 1
        first += 1
        second += 1
    return -1


def two_sum_v2(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        total = nums[left] + nums[right]

        if total == target:
            return [left + 1, right + 1]
        if total > target:
            right -= 1
        elif total < target:
            left += 1


def three_sum(nums):
    nums.sort()

    result = []
    for index in range(0, len(nums)):
        left = index + 1
        right = len(nums) - 1
        while left < right:
            if nums[index] + nums[left] + nums[right] == 0:
                result.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1
            if nums[index] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1

    return result


def group_anagram(strs):
    counter = {}

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if counter.get(sorted_s) is None:
            counter[sorted_s] = [s]
        else:
            counter[sorted_s].append(s)

    return list(counter.values())


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    ans = 0
    while left <= right:
        ans = max(ans, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans


def summary_ranges(nums: List[int]) -> int:
    set_nums = set(nums)
    intervals = []

    for num in nums:
        if num - 1 not in set_nums:
            len = 1
            interval = f"{num}->"
            while num + len in set_nums:
                len += 1
            if num + len - 1 == num:
                interval = f'{num}'
            else:
                interval += f'{num + len - 1}'
            intervals.append(interval)
    return intervals


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
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


def insert_intervals(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    for i, interval in enumerate(intervals):
        if new_interval[0] > interval[1]:
            result.append(interval)
        elif interval[0] < new_interval[0]:
            return result + new_interval + intervals[i:]
        else:
            new_interval = (min(interval[0], new_interval[0]), max(interval[1], new_interval[1]))
    return result + new_interval


def find_min_arrow_shoots(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] > result[-1][1]:
            result.append(interval)
    return len(result)


def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


def interaction_arrays_2(nums1, nums2):
    """
    Даны два массива целых чисел nums1 и nums2. Верните массив их пересечения. Каждый элемент в результате должен
    встречаться столько раз, сколько он встречается в обоих массивах, и вы можете возвращать результат в любом порядке.
    """

    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    answer = []
    for i in nums2:
        for index, j in enumerate(nums1):
            if i == j:
                answer.append(i)
                nums1.pop(index)
                break
    return answer


def contains_duplicate(nums):
    """
    Дан целочисленный массив nums. Верните true, если какое-либо значение встречается в массиве хотя бы дважды, и false, если все элементы различны.
    """
    counter = {}
    for num in nums:
        if counter.get(num) == 1:
            return True
        counter[num] = counter.get(num, 0) + 1
    return False


def valid_palidrome(s: str):
    preprare_s = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            preprare_s += i.lower()

    for i in range(len(preprare_s)):
        if preprare_s[i] != preprare_s[i * -1 - 1]:
            return False
    return True


def longest_subsrring_without_repeat(s: str) -> int:
    """
    Дана строка s. Найдите длину самой длинной подстроки без повторяющихся символов.
    """
    char_index = {}  # Хранит {символ: последний_индекс}
    left = 0
    max_length = 0
    for right in range(len(s)):
        current_char = s[right]
        # Если символ уже встречался и находится в текущем окне
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1  # Сдвигаем левую границу
        # Обновляем позицию символа
        char_index[current_char] = right
        # Обновляем максимальную длину
        max_length = max(max_length, right - left + 1)
    return max_length


def longest_polindromic_substring(s: str) -> int:
    """
    Для заданной строки s найдите самую длинную палиндромную подстроку в строке s.
    """
    """
    Решение в лоб за O(n3)
    """
    max_polindromic_substring = ''
    for i in range(len(s)):
        current_polindromic_substring = s[i]
        for j in range(i + 1, len(s) + 1):
            if s[i:j][::-1] == s[i:j]:
                if len(current_polindromic_substring) < len(s[i:j]):
                    current_polindromic_substring = s[i:j]
        if len(current_polindromic_substring) > len(max_polindromic_substring):
            max_polindromic_substring = current_polindromic_substring
    return max_polindromic_substring


def longest_polindromic_substing_v2(s: str) -> int:
    longest = ""
    for i in range(len(s)):
        for left, right in [(i, i), (i, i + 1)]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(longest) < right - left:
                longest = s[left + 1:right]
    return longest


def increasing_triplet_sybseq(nums: str) -> int:
    first, second = float('inf'), float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


def rle_count(n):
    """
    Последовательность подсчитай и скажи — это последовательность цифровых строк, определяемая рекурсивной формулой:

    countAndSay(1) = "1"
    countAndSay(n) Это кодирование длин серий для countAndSay(n - 1).
    Кодирование длин серий (RLE) — это метод сжатия строк, при котором последовательные одинаковые символы (повторяющиеся 2 или более раз) заменяются конкатенацией символа и числа, обозначающего количество символов (длину серии). Например, чтобы сжать строку "3322251", мы заменяем "33" на "23", заменяем "222" на "32", заменяем "5" на "15" и заменяем "1" на "11". Таким образом, сжатая строка становится "23321511".

    Для заданного положительного целого числа n верните этот nth элемент подсчёта и вывода последовательности.
    """

    def generate_rle_s(s):
        current_s = s[0]
        count_current_s = 1
        if len(s) == 1:
            return f'{count_current_s}{current_s}'

        rle_s = ''
        for i in range(1, len(s)):
            if current_s != s[i]:
                rle_s += f'{count_current_s}{current_s}'
                current_s = s[i]
                count_current_s = 1
            else:
                count_current_s += 1
        rle_s += f'{count_current_s}{current_s}'

        return rle_s

    count_rle_s = '1'
    for i in range(n - 1):
        count_rle_s = generate_rle_s(count_rle_s)
    return count_rle_s
