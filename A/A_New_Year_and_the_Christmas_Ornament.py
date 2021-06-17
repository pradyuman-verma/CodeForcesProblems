def ans(arr):
    y, b, r =arr[0], arr[1], arr[2]
    return (min(y + 2, min(b + 1, r)) * 3) - 3
if __name__ == '__main__':
    ybr = list(map(int, input().strip().split()))
    print(ans(ybr))