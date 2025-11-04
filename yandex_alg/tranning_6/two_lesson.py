def pref_sum():
    n = int(input()) + 1
    arr = list(map(int, input().split(" ")))
    prefixsum = [0] * n
    for i in range(1, n):
        prefixsum[i] = prefixsum[i - 1] + arr[i - 1]

    print(' '.join(list(map(str, prefixsum[1:]))))


def sum_number_car():
    n, k = list(map(int, input().split(" ")))
    cars = list(map(int, input().split(" ")))
    L = 0
    R = 0

    count = 0
    while R <= n - 1:
        num_cars = cars[L] if L == R else sum(cars[L:R + 1])
        if num_cars > k:
            L += 1
            continue
        if k - num_cars <= 0:
            count += 1
        R += 1
    print(count)


def sum_number_car_2():
    n, k = list(map(int, input().split(" ")))
    cars = list(map(int, input().split(" ")))

    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + cars[i - 1]
    count = 0
    j = 0
    for i in range(len(prefixsum)):
        while j < len(prefixsum) and prefixsum[j] - prefixsum[i] < k:
            j += 1
        if j == len(prefixsum):
            break
        if prefixsum[j] - prefixsum[i] == k:
            count += 1
    print(count)


def city_ch():
    n, k = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))

    i, j, count = 0, 1, 0

    while j < len(nums) and i < len(nums) - 1:
        if nums[j] - nums[i] <= k:
            j += 1
        else:
            count += n - j
            i += 1
    print(count)


def bast_vacation():
    with open("C:\\Users\\Admin\\PycharmProjects\\ToTopSkills\\yandex_alg\\tranning_6\\21", 'r') as file:
        n, k = [int(i) for i in file.readline().split(" ")]
        nums = list(map(int, file.readline().split(" ")))
    nums.sort()

    r = 1
    count = 0
    for i, num in enumerate(nums):
        l = num
        while r <= len(nums) - 1:
            if nums[r] - l > k:
                l = nums[r]
                nums.pop(r)
            else:
                r += 1
        count += 1
        r = i
    print(count)


def best_vacation_2():
    with open("C:\\Users\\Admin\\PycharmProjects\\ToTopSkills\\yandex_alg\\tranning_6\\21", 'r') as file:
        n, k = [int(i) for i in file.readline().split(" ")]
        nums = list(map(int, file.readline().split(" ")))
    nums.sort()

    l = 0
    r = 0
    count = 0
    while len(nums) != 0:
        point = nums.pop(l)
        while r <= len(nums) - 1:
            if nums[r] - point > k:
                point = nums.pop(r)
            else:
                r += 1
        r = 0
        count += 1
    print(count)


def best_vacation_3():
    with open("C:\\Users\\Admin\\PycharmProjects\\ToTopSkills\\yandex_alg\\tranning_6\\25", 'r') as file:
        n, k = [int(i) for i in file.readline().split(" ")]
        nums = list(map(int, file.readline().split(" ")))
    nums.sort()

    l = 0
    r = 0
    groups = []
    while nums[r] - nums[l] <= k:
        groups.append([nums[r]])
        r += 1
        if r > len(nums) - 1:
            break
    nums_r = nums[r:]
    r = 0
    while r < len(nums_r):
        if nums_r[r] - groups[l][-1] > k:
            groups[l].append(nums_r.pop(r))
            l += 1
        else:
            groups.append([nums_r.pop(r)])
        if l > len(groups) - 1:
            l = 0
    print(len(groups))


def best_vacation_4():
    with open("C:\\Users\\Admin\\PycharmProjects\\ToTopSkills\\yandex_alg\\tranning_6\\23", 'r') as file:
        n, k = [int(i) for i in file.readline().split(" ")]
        nums = list(map(int, file.readline().split(" ")))
    nums.sort()

best_vacation_4()


def help_odd(result, nums):
    point = len(nums) // 2
    result.append(str(nums.pop(point)))


def help_even(result, nums):
    point = (len(nums) // 2) - 1
    result.append(str(nums.pop(point)))


def removing_medians():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    nums.sort()
    result = []
    if len(nums) % 2 != 0:
        while len(nums) != 0:
            help_odd(result, nums)
            if len(nums) == 0:
                break
            help_even(result, nums)
    else:
        while len(nums) != 0:
            help_even(result, nums)
            if len(nums) == 0:
                break
            help_odd(result, nums)
    print(" ".join(result))


def sum_three():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    nums.sort()
    l = 0
    r = 3
    result = []
    while r <= len(nums):
        if 1 <= nums[l] < nums[r - 2] < nums[r - 1]:
            mull_window = 1
            for i in nums[l:r]:
                mull_window *= i
            if len(result) == 0:
                result.append(mull_window)
            elif result[-1] < mull_window:
                result.append(mull_window)
        l += 1
        r += 1
    print(result[-1])

sum_three()
