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


import sys


def number_words_text():
    with open(sys.argv[1], 'r') as file:
        contents = file.read()

    arr = contents.replace('\n', ' ').split(' ')
    arr.extend([' ', '\n'])
    print(len(set(arr)))


def open_calculator():
    nums = {i for i in input().split(' ')}
    number = {i for i in input()}
    count = len(number - nums)
    print(count)


def alien_genome():
    genome_one = input().upper()
    genome_two = input().upper()
    arr_couple_genome = {f'{genome_one[idx]}{genome_one[idx + 1]}' for idx in range(0, len(genome_one) - 1)}
    set_couple_genome = {f'{genome_two[idx]}{genome_two[idx + 1]}' for idx in range(0, len(genome_two) - 1)}

    count = 0
    for couple_genome in arr_couple_genome:
        if set_couple_genome & {couple_genome}:
            count += 1
    print(count)


def polyglots():
    count_polyglots = int(input())

    union_lang = set()
    inter_lang = set()
    for i in range(0, count_polyglots):
        lang = {str(input()) for _ in range(0, int(input()))}
        if inter_lang == set():
            inter_lang = lang
        union_lang = union_lang | lang
        inter_lang = inter_lang & lang

    print(len(inter_lang))
    for i in union_lang:
        print(i)
    print(len(union_lang))
    for i in union_lang:
        print(i)


polyglots()
