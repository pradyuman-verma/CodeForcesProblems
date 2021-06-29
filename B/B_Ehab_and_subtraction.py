def ans(arr):
    arr = sorted(list(set(arr)))
    print(arr[0])
    xx = min(len(arr), k)
    cnt = arr[0]
    for i in range(1, xx):
        if(arr[i] - cnt > 0):
            print(arr[i] - cnt)
            cnt += arr[i] - cnt
        else:
            continue   
    if(k > xx):
        for _ in range(k - xx):
            print(0)
if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    n = nk[0]
    k = nk[1]
    a = list(map(int, input().strip().split()))
    ans(a)