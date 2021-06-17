def ans(n):
    return([1] * n)

if __name__ == '__main__':
    n = int(input())
    result = ans(n)
    print(len(result))
    print(*result)