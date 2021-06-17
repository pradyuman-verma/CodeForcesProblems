def ans(n, v):
    cnt = 0
    if(v >= n):
        return(n - 1)
    else:
        cnt += v
        for i in range(1, n - v + 1):
            cnt += i
        return cnt - 1

if __name__ == '__main__':
    nv = list(map(int, input().strip().split()))
    n, v = nv[0], nv[1]
    print(ans(n, v))