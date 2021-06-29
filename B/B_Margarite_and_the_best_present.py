def ans(l, r):
    n = r - l + 1
    if(l == r):
        if(l % 2):
            return(-1 * l)
        else:
            return(l)
    if(n % 2 == 0):
        if(abs(l) % 2 == 0):
            return(-1 * n // 2)
        else:
            return(n // 2)
    else:
        if(abs(l) % 2 == 0):
            ans = - 1 * n // 2
            ans += r
            return ans + 1
        else:
            ans = n // 2
            ans -= r
            return(ans)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = list(map(int, input().strip().split()))
        print(ans(n[0], n[1]))