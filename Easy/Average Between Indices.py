def solve(n, arr, x, y):
    count, sum = 0, 0
    for i in range(x, y + 1):
        count += 1
        sum += arr[i]
    return (sum / count)