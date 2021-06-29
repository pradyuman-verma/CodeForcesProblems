def ans(arr):
    arr.sort()
    arr1 = arr[0 : n // 2]
    arr2 = arr[n // 2 : n]
    arr2.reverse()
    cnt = 0
    for (i, j) in zip(arr1, arr2):
        cnt += (i + j) ** 2
    return cnt

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))