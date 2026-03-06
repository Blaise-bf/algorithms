

def binary_search(arr: list[int], target: int):

    left, right = 0, len(arr) - 1
        
    while left <= right:
        mid = left + right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 


def recursive_binary_search(arr: list[int], target: int, left: int, right: int):

    if left > right:
        return

    mid = left + right // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1 , right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1 )

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    
    print(binary_search(arr, target))
    print('------------------\n')
    print(f'Recursive: {recursive_binary_search(arr, target, 0, len(arr) - 1)}')
