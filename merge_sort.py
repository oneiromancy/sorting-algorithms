def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left_half = arr[:midpoint]
    right_half = arr[midpoint:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged_arr = []

    while (left and right):
        if left[0] < right[0]:
            merged_arr.append(left[0])
            left.pop(0)
        else:
            merged_arr.append(right[0])
            right.pop(0)

    if left:
        merged_arr += left
    if right:
        merged_arr += right

    return merged_arr
