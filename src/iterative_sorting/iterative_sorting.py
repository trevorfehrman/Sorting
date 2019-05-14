import math


def selection_sort(arr):
    smallest = math.inf
    smallest_index = None

    for i in range(len(arr)):

        for j in range(i, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]  # Swap values
        smallest = math.inf

    return arr


selection_sort([5, 1, 89, 23, 1, 56, 23, 47])


def bubble_sort(arr):
    swapped = True
    while(swapped):
        swapped = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]  # Swap values
                swapped = True

    return arr


bubble_sort([5, 1, 89, 23, 1, 56, 23, 47])

# STRETCH: implement the Count Sort function below


# def count_sort(arr, maximum=-1):

#     return arr
