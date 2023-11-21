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

