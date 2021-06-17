def ans(arr):
    s, a, b, c = arr[0], arr[1], arr[2], arr[3]
    return (s // (c * a)) * b + (s // c)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        sabc = list(map(int, input().strip().split()))
        print(ans(sabc))