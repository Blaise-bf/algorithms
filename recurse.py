import array
from operator import le
from token import GREATER


def count_down(n: int):
    if n < 0:
        print()
        return
    print(n, end=" ")
    count_down(n - 1)

def count_up(n: int):
    if n > 10:
        print()
        return
    print(n, end=" ")
    count_up(n + 1)


def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sum_list(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + sum_list(arr[1:])



def quick_sort(arr: list[int]) -> list[int]:

    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    great = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(great)

