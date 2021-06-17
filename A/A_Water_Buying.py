def ans(arr):
    n, a, b = nab[0], nab[1], nab[2]
    tb = n % 2
    ta = n - tb
    ta = ta // 2
    cnt1 = (ta * b) + (tb * a)
    return(min(cnt1, a * n))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        nab = list(map(int, input().strip().split()))
        print(ans(nab))