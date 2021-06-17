def ans(arr):
    i = 1
    cnt = 0
    while i <= n:
        cnt += 1
        mx = i
        while i <= n and i <= mx:
            mx = max(mx, arr[i - 1])
            i += 1
    return(cnt) 
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))