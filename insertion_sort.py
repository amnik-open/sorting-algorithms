def insertion_sort(numbers):
    for i in range(len(numbers)):
        j = i
        while j > 0:
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            else:
                break
            j -= 1
    return numbers


num = list(map(int, input().split()))
print(insertion_sort(num))
