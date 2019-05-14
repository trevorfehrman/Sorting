import math


def merge(arrA, arrB):
    i = 0
    j = 0
    sorted = []
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            sorted.append(arrA[i])
            i += 1
        else:
            sorted.append(arrB[j])
            j += 1
    sorted.extend(arrA[i:])
    sorted.extend(arrB[j:])
    return sorted


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = math.floor(len(arr) / 2)
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


print(merge_sort([1, 6, 7, 8, 43, 4, 656, 7, 8]))


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
