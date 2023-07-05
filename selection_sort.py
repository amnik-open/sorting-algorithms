def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers


num = list(map(int, input().split()))
print(selection_sort(num))