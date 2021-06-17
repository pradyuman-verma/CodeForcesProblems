def ans(arr):
    Min = float('inf')
    for i in range(0, n):
        min_ = 0
        for j in range(1, n):
            min_ += 2 * (abs(i - j) + i + j) * arr[j]
        Min = min(Min, min_)
    return(Min)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))
        