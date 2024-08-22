from collections import defaultdict
from itertools import groupby


def dict_synonyms():
    count = int(input())
    synonyms = {}
    for _ in range(0, count):
        words = input().split(' ')
        synonyms.update({words[0]: words[1], words[1]: words[0]})
    input_word = str(input())

    print(synonyms[input_word])


import sys


def number_word_appearance():
    with open(sys.argv[1], 'r') as file:
        contents = file.read()
    arr_words = contents.replace('\n', ' ').split(' ')
    dct = {}
    new_arr = []
    for index in range(0, len(arr_words)):
        if arr_words[index] not in dct.keys():
            dct[arr_words[index]] = 0
            new_arr.append('0')
            continue
        dct[arr_words[index]] += 1
        new_arr.append(str(dct[arr_words[index]]))
    print(' '.join(new_arr))


def most_common_word():
    words = input().split(' ')
    ascii_litters = 'abcdefghijklmnopqrstuvwxyz'
    alpha_num = {ascii_litters[index]: index + 1 for index in range(0, len(ascii_litters))}
    words_num = {}
    count = 0
    for word in words:
        words_num[word] = words_num.get(word, 0) + 1
        if count < words_num[word]:
            count += 1

    arr = []
    for key, value in words_num.items():
        if count == value:
            arr.append(key)

    return sorted(arr)[0]


def keyboard():
    from collections import Counter
    count_keys = int(input())
    count_clicks = input().split(' ')
    count_clicks = {i + 1: int(count_clicks[i]) for i in range(0, len(count_clicks))}

    total_clicks = int(input())
    counter_clicks = Counter(input().split(' '))
    for key, count in counter_clicks.items():
        print('YES') if count_clicks[int(key)] < count else print('NO')


def pyramid():
    count_blocks = int(input())
    dct = {}
    for i in range(0, count_blocks):
        w, h = [int(i) for i in input().split(' ')]
        if w not in dct:
            dct[w] = h
        if w in dct and h > dct[w]:
            dct[w] = h
    print(sum(dct.values()))


def sales():
    file = input().split('\n')
    dct: {str: dict} = {}
    for data in file:
        fio, product, count = data.split(' ')
        if fio not in dct:
            dct[fio] = {product: count}
        else:
            if product not in dct[fio]:
                dct[fio].update({product: count})
            else:
                dct[fio].update({product: int(dct[fio][product]) + int(count)})
    print(sorted(dct.items()))


def error():
    n = int(input())
    total = 0
    arr = []
    for i in range(n):
        a, b = [int(i) for i in input().split(' ')]
        arr.append(a * b)
        total += a * b

    for i in arr:
        print(i / total)


def middle_element():
    arr = [int(i) for i in input().split(' ')]

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[1]


def unique_elements():
    n = int(input())
    arr = [int(i) for i in input().split(' ')]

    counter = {}
    for i in arr:
        counter[i] = counter.get(i, 0) + 1

    unique = 0
    for i in counter.values():
        if i == 1:
            unique += 1
    print(unique)


def stones_jewelry():
    J = [i for i in input()]
    S = input()
    count = 0
    for i in S:
        if i in J:
            count += 1
    print(count)


def common_elements(a, b):
    b_dict = defaultdict(int)
    for el in b:
        b_dict[el] += 1  # я считаю все элементы из b, т.е. типа collections.Counter

    result = []
    for el in a:
        if b_dict[el] > 0:  # если какой-то элемент из a встречается в b
            result.append(el)  # то это успех
            b_dict[el] -= 1  # и я "вынимаю" его из b, т.е. уменьшаю его количество на 1
    return result


def convert(s):
    current_word = s[0]
    current_word_count = 1
    result = ''
    for word in list(s[1:]) + [None]:
        if current_word != word:
            result += f'{current_word}{current_word_count}'
            current_word_count = 1
            current_word = word
        else:
            current_word_count += 1
    print(result)


def interval(lst):
    sorted_lst = sorted(lst)
    interval_start = sorted_lst[0]
    interval_end = sorted_lst[0]
    result = ''
    for i in range(0, len(sorted_lst[1:])):
        if sorted_lst[i] + 1 != sorted_lst[i + 1]:
            result += f'interval_start' if interval_start == interval_end else f'{interval_start}-{interval_end}'
            interval_start = sorted_lst[i + 1]
            interval_end = sorted_lst[i + 1]
        else:
            interval_end = sorted_lst[i + 1]
    print(result)

