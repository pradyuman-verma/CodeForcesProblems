def ans(arr):
    cnt = 1
    ans = 0
    cnt1 = 1
    i = 1
    while i < n:
        if(arr[i] == arr[i - 1]):
            cnt += 1
        else:
            cnt1 = cnt
            cnt = 1
        ans = max(ans, min(cnt, cnt1))
        i += 1
    return ans * 2

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().strip().split()))
    print(ans(t))