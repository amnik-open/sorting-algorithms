import random


def partition(numbers, l, r):
    m = random.randint(l, r)
    numbers[l], numbers[m] = numbers[m], numbers[l]
    j = l
    for i in range(l + 1, r + 1):
        if numbers[l] >= numbers[i]:
            j = j + 1
            numbers[j], numbers[i] = numbers[i], numbers[j]
    numbers[l], numbers[j] = numbers[j], numbers[l]
    return j


def partition3(numbers, l, r):
    m2 = partition(numbers, l, r)
    m1 = m2
    i = l
    while i < m1:
        if numbers[i] == numbers[m2]:
            m1 -= 1
            numbers[i], numbers[m1] = numbers[m1], numbers[i]
        i += 1
    return m1, m2


def quick_sort(numbers, l, r):
    if l >= r:
        return
    m1, m2 = partition3(numbers, l, r)
    quick_sort(numbers, l, m1 - 1)
    quick_sort(numbers, m2 + 1, r)


num = list(map(int, input().split()))
quick_sort(num, 0, len(num) - 1)
print(num)
