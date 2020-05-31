import random


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


def gcd_recursive(n1, n2):
    # greatest common divider
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    if n1 > n2:
        return gcd_recursive(n2, n1 % n2)
    else:
        return gcd_recursive(n1, n2 % n1)


def gcd_cycle(n1, n2):
    # greatest common divider
    a = max(n1, n2)
    b = min(n1, n2)
    while b != 0:
        a, b = b, a % b
    return a


def buble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


def quick_sort(array):
    if len(array) <= 1:
        return array

    supposed = array[0]
    left = [n for n in array[1:] if n < supposed]
    right = [n for n in array[1:] if n >= supposed]

    return quick_sort(left) + [supposed] + quick_sort(right)


def merge_sort(array):
    def merge(a1, a2):
        i = 0
        k = 0
        c = []

        while i < len(a1) and k < len(a2):
            if a1[i] < a2[k]:
                c.append(a1[i])
                i += 1
            else:
                c.append(a2[k])
                k += 1

        c = c + a1[i:] + a2[k:]

        return c

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def binary_search(sorted_array, key):
    def left_bound(sorted_array, key):
        left = -1
        right = len(sorted_array)
        while right - left > 1:
            middle = (right + left) // 2
            if sorted_array[middle] < key:
                left = middle
            else:
                right = middle
        return left

    def right_bound(sorted_array, key):
        left = -1
        right = len(sorted_array)
        while right - left > 1:
            middle = (right + left) // 2
            if sorted_array[middle] <= key:
                left = middle
            else:
                right = middle
        return right

    return left_bound(sorted_array, key), right_bound(sorted_array, key)


def fib(n):
    if n <= 0:
        return None
    if n <= 2:
        return 1
    f1 = 1
    f2 = 2
    for i in range(3, n):
        f1, f2 = f2, f1 + f2

    return f2




# a = [random.randint(0,10) for i in range(10)]
# print(a)
# a =merge_sort(a)
# print(a)
# key = 5
# print(key)
# print(binary_search(a,key))
