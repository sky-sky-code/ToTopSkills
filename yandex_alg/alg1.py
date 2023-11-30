import math


def ambulance(k1, m, k2, p2, n2):
    rooms_on_floor = math.ceil(k2 / n2)
    count_rooms_on_floor = ((m - n2) * rooms_on_floor) + k2

    n1 = p2
    while count_rooms_on_floor < k1:
        n1 += 1
        count_rooms_on_floor += count_rooms_on_floor

    down_floor_to_my_room = m - ((count_rooms_on_floor - k1) // rooms_on_floor)
    return n1, down_floor_to_my_room


def finder(arr):
    myset = set(arr)
    max_length = 0
    for num in arr:
        if num - 1 not in myset:
            curr_length = 1
            while num + 1 in myset:
                num += 1
                curr_length += 1
            max_length = max(max_length, curr_length)

    return max_length


def max_sides():
    a, b, c, d = map(int, input().split())
    l = []
    l.append(max(a, c) * (b + d))
    l.append(max(a, d) * (b + c))
    l.append(max(b, c) * (a + d))
    l.append(max(b, d) * (a + c))
    if min(l) == l[0]:
        print(max(a, c), b + d)
    elif min(l) == l[1]:
        print(max(a, d), b + c)
    elif min(l) == l[2]:
        print(max(b, c), a + d)
    else:
        print(max(b, d), a + c)


def underg():
    int1 = int(input())
    int2 = int(input())
    k1 = int(input())
    k2 = int(input())
    min1 = k1 + int1 * (k1 - 1)
    max1 = k1 + int1 * (k1 + 1)
    min2 = k2 + int2 * (k2 - 1)
    max2 = k2 + int2 * (k2 + 1)

    if max1 > max2:
        tmax = max2
    else:
        tmax = max1
    if min1 > min2:
        tmin = min1
    else:
        tmin = min2
    if tmin > tmax:
        print(-1)
    else:
        print(tmin, tmax)


def type_seq():
    n = int(input())
    CONSTANT = 0
    ASCENDING = 0
    DESCENDING = 0

    while n != -2000000000:
        new_n = int(input())
        if new_n == -2000000000:
            break
        if new_n == n:
            CONSTANT += 1
        elif new_n > n:
            ASCENDING += 1
        elif new_n < n:
            DESCENDING += 1
        n = new_n
    if ASCENDING != 0 and DESCENDING != 0:
        return "RANDOM"
    elif ASCENDING == 0 and DESCENDING == 0:
        return 'CONSTANT'
    elif CONSTANT != 0 and ASCENDING > 0:
        return 'WEAKLY ASCENDING'
    elif CONSTANT != 0 and DESCENDING > 0:
        return 'WEAKLY DESCENDING'
    elif ASCENDING > 0:
        return 'ASCENDING'
    elif DESCENDING > 0:
        return "DESCENDING"


def nearest_number():
    n = int(input())
    nums = [int(i) for i in input().split(' ')]
    number = int(input())

    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    low = 0
    high = len(nums) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == number:
            break
        if nums[mid] < number:
            low = mid + 1
        elif nums[mid] > number:
            high = mid - 1
    return nums[mid]


def more_your_neighbors():
    nums = [int(i) for i in input().split(' ')]
    count = 0
    index = 1
    finish = len(nums) - 1
    while index < finish:
        if nums[index + 1] > nums[index]:
            index += 1
            continue
        if nums[index - 1] < nums[index] > nums[index + 1]:
            count += 1
            if index + 2 > finish:
                break
            index += 2
        else:
            index += 1
    print(count)


def symmetric_sequence():
    nums = [int(i) for i in input().split(' ')]
    mid = len(nums) // 2 + 1
    point = mid

    if nums[0:mid - 1] == nums[mid + 1:]:
        return print(0)

    for index in range(mid, len(nums)):
        if index + 1 >= len(nums):
            break
        elif nums[index] < nums[index + 1] or nums[index] > nums[index + 1]:
            point += 1

    print(len(nums[:point]))
    print(nums[:point][::-1])


symmetric_sequence()
