def quick_sort(arr, low, high):

    # checking if low is smaller then high
    # if not then array part is already sorted
    if low < high:

        # calling partition function
        # it will put pivot on correct position
        pivot = partition(arr, low, high)

        # sorting left side of pivot
        quick_sort(arr, low, pivot - 1)

        # sorting right side of pivot
        quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):

    # taking first element as pivot
    p = arr[low]

    # i start from left side
    i = low + 1

    # j start from right side
    j = high

    while True:

        # moving i to right until bigger element found
        while i <= j and arr[i] <= p:
            i += 1

        # moving j to left until smaller element found
        while i <= j and arr[j] >= p:
            j -= 1

        # if i is smaller then j swap both values
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

        # if i cross j then stop loop
        else:
            break

    # swapping pivot with j position
    # now pivot is on correct place
    arr[low], arr[j] = arr[j], arr[low]

    # returning pivot index
    return j


# array for sorting
arr = [2,4,6,1,6,82,3,5,7,9,3]

# calling quick sort function
quick_sort(arr, 0, len(arr)-1)

# printing sorted array
print(arr)