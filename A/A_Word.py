def ans(arr):
    up_cnt, lo_cnt = 0, 0
    for i in range(len(arr)):
        if(arr[i].islower()):
            lo_cnt += 1
        else:
            up_cnt += 1
    if(lo_cnt >= up_cnt):
        return(''.join(arr).lower())
    return(''.join(arr).upper()) 

if __name__ == '__main__':
    n = list(input())
    print(ans(n))