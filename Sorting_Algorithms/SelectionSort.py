def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1,n):
            if arr[j] < arr[mini]:
                mini = j
                arr[mini], arr[i] = arr[i], arr[mini]

array = [42, 17, 23, 8, 34, 50, 1]
selection_sort(array)
print(array)


