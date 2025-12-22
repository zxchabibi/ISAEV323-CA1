def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return left_max if left_max > right_max else right_max
numbers = [3, 7, 1, 9, 4, 2]
print(find_max(numbers))  