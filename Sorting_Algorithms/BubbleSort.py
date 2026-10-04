def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j  + 1] = arr[j + 1],arr[j]

array = [12, 5, 8, 19, 3, 15, 7]

bubble_sort(array)
print(array)