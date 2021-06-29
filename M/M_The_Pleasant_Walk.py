def ans(arr):
    cnt = 0
    cnt1 = 0
    i = 0
    while i < n - 1:
        if(arr[i] != arr[i + 1]):
            cnt += 1
        else:
            cnt1 = max(cnt1, cnt)
            cnt = 0
        i += 1
    cnt1 = max(cnt1, cnt)
    return(cnt1 + 1)

if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    n, k = nk[0], nk[1]
    a = list(map(int, input().strip().split()))
    print(ans(a))