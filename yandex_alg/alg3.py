def different_numbers():
    nums = {int(i) for i in input().split(' ')}
    print(len(nums))


def intersection():
    set_1 = {int(i) for i in input().split(' ')}
    set_2 = {int(i) for i in input().split(' ')}
    for i in sorted(set_1 & set_2):
        print(i, end=' ')


def cubes():
    cubes = []
    for count_cubes in input().split(' '):
        cubes_color = set()
        for j in range(int(count_cubes)):
            cubes_color.add(int(input()))
        cubes.append(cubes_color)

    operation_set = {
        '&': lambda a, b: [len(a & b), ' '.join([str(i) for i in sorted(a & b)])],
        '-': lambda a, b: [
            len(a - b), ' '.join([str(i) for i in sorted(a - b)]),
            len(b - a), ' '.join([str(i) for i in sorted(b - a)])
        ]
    }

    for key in operation_set:
        operation_result = operation_set[key](cubes[0], cubes[1])
        for result in operation_result:
            print(result)


