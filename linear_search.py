def linear_search(arr: list, target):
    """
    Perform a linear search for the target value in the given array.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example usage:
if __name__ == "__main__":
    my_array = [5, 3, 2, 8, 1]
    target_value = 2
    result = linear_search(my_array, target_value)
    linear_search(my_array, target_value)
    if result != -1:
        print(f"Target {target_value} found at index: {result}")
    else:
        print(f"Target {target_value} not found in the array.")
