def solve(n, arr):
    # Typecast the list to a set to remove the duplicates
    arr_set = set(arr)

    arr = list(arr_set)

    # Sort the array (list) in descending order to get the largest elements first
    arr.sort(reverse=True)

    return arr[1]


print(solve(5, [4, 2, 3, 2, 5]))
