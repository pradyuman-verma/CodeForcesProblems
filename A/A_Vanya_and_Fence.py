def ans(arr):
    cnt = 0
    for i in range(n):
        if(arr[i] > h):
            cnt += 2
        else:
            cnt += 1
    return(cnt)

if __name__ == '__main__':
    nh = list(map(int, input().strip().split()))
    n, h = nh[0], nh[1]
    a = list(map(int, input().strip().split()))
    print(ans(a))