def ans(arr):
    k, x = arr[0], arr[1]
    return((9 * (k - 1)) + x)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().strip().split()))
        print(ans(a))