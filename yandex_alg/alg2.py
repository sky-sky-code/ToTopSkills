def list_grow():
    n = [int(i) for i in input().split(' ')]
    for index in range(len(n) - 1):
        if not n[index] < n[index + 1]:
            return 'NO'
    return 'YES'


def type_sequence():
    el_seq = int(input())
    CONSTANT = 0
    ASCENDING = 0
    DESCENDING = 0

    while el_seq != -2000000000:
        next_el_seq = int(input())
        if next_el_seq == -2000000000:
            break
        if el_seq == next_el_seq:
            CONSTANT += 1
        elif el_seq < next_el_seq:
            ASCENDING += 1
        elif el_seq > next_el_seq:
            DESCENDING += 1

        el_seq = next_el_seq

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


def nearest_value(items, value):
    '''Поиск ближайшего значения до value в списке items'''

    found = items[0]  # найденное значение (первоначально первое)
    for item in items:
        print(abs(item - value), abs((found - value)))
        if abs(item - value) < abs(found - value):
            found = item
    return found


def more_neighbors():
    arr = [int(i) for i in input().split(' ')]

    count = 0
    index = 1
    while index < len(arr) - 1:
        if arr[index - 1] < arr[index] > arr[index + 1]:
            count += 1
        index += 1
    print(count)


def symmetric_sequence():
    lst = input().split()
    for i in range(len(lst)):
        if lst[i:] == lst[i:][::-1]:
            print(i)
            print(*lst[:i][::-1])
            break


def largest_numbers():
    nums = sorted([int(i) for i in input().split(' ')])
    if nums[0] * nums[1] > nums[-1] * nums[-2]:
        print(nums[0], nums[1])
    else:
        print(nums[-2], nums[-1])

