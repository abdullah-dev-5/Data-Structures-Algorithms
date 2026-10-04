def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1 
        key = arr[j + 1]

array = [9, 14, 2, 27, 6, 18, 11]

insertion_sort(array)
print(array)