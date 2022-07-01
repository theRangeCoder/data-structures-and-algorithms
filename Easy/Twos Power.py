def solve(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 0 + solve(n / 2)
        else:
            return 0


print(solve(67))