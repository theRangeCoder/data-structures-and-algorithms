def solve(n, arr):
    # Convert list to a set to remove the duplicates
    arr_2 = set(arr)

    # Convert set to a list again for easier comparison
    arr_2 = list(arr_2)

    # Sorting the two lists in ascending order to facilitate a convenient comparison of elements
    arr.sort()
    arr_2.sort()

    if arr == arr_2:
        return 0
    else:
        return 1

print(solve(4, [2, 3, 1, 1]))