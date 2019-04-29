# TO-DO: Complete the selection_sort() function below
import math


def selection_sort(arr):
    smallest = math.inf
    smallest_index = None
    temp = None

    for i in range(len(arr)):

        for j in range(i, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        smallest = math.inf
    print(arr)
    return arr


selection_sort([5, 1, 89, 23, 1, 56, 23, 47])
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True
    temp = None
    while(swapped):
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swapped = True
    # print(arr)
    return arr


bubble_sort([5, 1, 89, 23, 1, 56, 23, 47])

# STRETCH: implement the Count Sort function below


# def count_sort(arr, maximum=-1):

#     return arr
