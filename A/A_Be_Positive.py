def ans(arr):
    cnt_p = 0
    cnt_n = 0
    for i in range(n):
        if(arr[i] > 0):
            cnt_p += 1
        if(arr[i] < 0):
            cnt_n += 1
    if(cnt_p >= (n + 1) // 2 ):
        return(1)
    elif(cnt_n >= (n + 1) // 2):
        return(-1)
    return(0)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))