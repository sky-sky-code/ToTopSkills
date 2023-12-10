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


def greatest_work():
    nums = [int(i) for i in input().split(' ')]

    arr = []

    count_loop = 0

    while count_loop != 2:
        max_num = 0
        index_max_num = 0

        for index in range(0, len(nums)):
            if len(arr) != 0:
                if arr[0] * nums[index] > max_num:
                    max_num = arr[0] * nums[index]
                    index_max_num = index
            if abs(nums[index]) > max_num:
                max_num = abs(nums[index])
                index_max_num = index

        arr.append(nums.pop(index_max_num))
        count_loop += 1

    print(arr[0], arr[1])


def greatest_work_v2():
    a = map(int, input().split())
    a = list(a)
    a = sorted(a)
    if a[0] * a[1] > a[len(a) - 1] * a[len(a) - 2]:
        print(a[0], a[1])
    else:
        print(a[-2], a[-1])


def greatest_work_with_3_num():
    nums = [int(i) for i in input().split()]
    nums = sorted(nums)
    if nums[0] * nums[1] * nums[-1] > nums[0] * nums[1] * nums[2] or nums[0] * nums[1] * nums[-1] > nums[-1] * nums[
        -2] * nums[-3]:
        print(nums[0] * nums[1] * nums[-1])
    if nums[0] * nums[1] * nums[2] > nums[-1] * nums[-2] * nums[-3]:
        print(nums[0], nums[1], nums[3])
    else:
        print(nums[-1], nums[-2], nums[-3])


def sapper():
    nums = [int(i) for i in input().split(' ')]
    count_rows = nums[0]
    count_columns = nums[1]
    count_bomb = nums[2]

    coordinate_bomb = []
    maap = []

    for bomb in range(0, count_bomb):
        coordinate_bomb.append([int(i) for i in input().split(' ') if i.isdigit()])

    for row in range(0, count_rows):
        maap.append([0 for _ in range(0, count_columns)])

    coordinate_neighbors = []

    for coordinate in coordinate_bomb:
        row, column = coordinate[0], coordinate[1]
        if row + 1 <= count_rows or column + 1 <= count_columns:
            if row + 1 <= count_rows and column + 1 <= count_columns:
                coordinate_neighbors.append([row + 1, column + 1])
            if column + 1 <= count_columns:
                coordinate_neighbors.append([row, column + 1])
            if row + 1 <= count_rows:
                coordinate_neighbors.append([row + 1, column])
            if column - 1 >= 0 and row + 1 <= count_rows:
                coordinate_neighbors.append([row + 1, column - 1])
        if row - 1 > 0 or column - 1 > 0:
            if row - 1 > 0 and column - 1 > 0:
                coordinate_neighbors.append([row - 1, column - 1])
            if column - 1 > 0:
                coordinate_neighbors.append([row, column - 1])
            if row - 1 > 0:
                coordinate_neighbors.append([row - 1, column])
            if row - 1 > 0 and column + 1 <= count_columns:
                coordinate_neighbors.append([row - 1, column + 1])

    for coordinate in coordinate_neighbors:
        row, column = coordinate[0], coordinate[1]
        if coordinate in coordinate_bomb:
            maap[row - 1][column - 1] = "*"
            continue
        maap[row - 1][column - 1] += 1

    for i in maap:
        print(i)
