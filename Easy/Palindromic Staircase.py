def solve(n):
    res_arr = []
    for i in range(1, n + 1):
        row_arr = []
        for j in range(1, i + 1):
            row_arr.append(str(j))
        for k in range(i - 1, 0, -1):
            row_arr.append(str(k))

        row_arr = ''.join(row_arr)
        res_arr.append(row_arr)

    return res_arr