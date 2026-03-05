from typing import List
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        swap = 0

        for j in range(0, n -i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap += 1

    print(f"Number of swaps: {swap}")

                # keep track of number of swaps
                # swaps += 1

                



    return arr

def bubble_sort_optimized(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        swaps = 0

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break
    print(f"Number of swaps: {swaps}")

    return arr



if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    sorted_arr_opt = bubble_sort_optimized(arr)
    print("Sorted array:", sorted_arr)
    print("Sorted array optimized:", sorted_arr_opt)



