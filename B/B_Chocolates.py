def ans(arr):
    cnt = arr[-1]
    summ = arr[-1]
    if(arr[-1] == 1):
        return(cnt)
    for i in range(n - 2, -1, -1):
        if(arr[i] < summ):
            cnt += arr[i]
            summ = arr[i]
        else:
            cnt += max(summ - 1, 0)
            summ = max(0, summ - 1)
    return cnt 

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))