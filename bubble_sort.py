def bubble_sort(arr):

    for num_checks in range(len(arr)):
        for el in range(len(arr) - num_checks - 1):
            if arr[el] > arr[el + 1]:
                arr[el], arr[el + 1] = arr[el + 1], arr[el]
