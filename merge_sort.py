def merge_sort(arr):
    if len(arr) == 1:
        return arr 

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr[k] = left[i]
            i += 1
        else:
            sorted_arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sorted_arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_arr[k] = right[j]
        j += 1
        k += 1

    return sorted_arr



# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)


