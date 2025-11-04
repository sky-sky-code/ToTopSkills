def raft():
    x1, y1, x2, y2, x, y = [int(input()) for i in range(6)]

    if x < x1:
        if y > y2:
            print('NW')
        elif y < y1:
            print('SW')
        else:
            print('W')
    elif x > x2:
        if y > y2:
            print('NE')
        elif y < y1:
            print('SE')
        else:
            print('E')
    else:
        if y > y2:
            print('N')
        else:
            print('S')


def t_shorts_and_socks():
    A, B, C, D = [int(input()) for i in range(4)]
    result = []

    if A > 0 and C > 0:
        result.append([A + 1, C + 1])
    if B > 0 and D > 0:
        result.append([B + 1, D + 1])
    if A > 0 and B > 0:
        result.append([max(A, B) + 1, 1])
    if C > 0 and D > 0:
        result.append([1, max(C, D) + 1])
    m = min(result, key=sum)
    print(*m)