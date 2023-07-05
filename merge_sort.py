def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    sub1 = numbers[:len(numbers) // 2]
    sub2 = numbers[len(numbers) // 2:]

    l = merge_sort(sub1)
    r = merge_sort(sub2)

    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            numbers[k] = l[i]
            i += 1
        else:
            numbers[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        numbers[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        numbers[k] = r[j]
        j += 1
        k += 1
    return numbers


numbers = list(map(int, input().split()))
print(merge_sort(numbers))
