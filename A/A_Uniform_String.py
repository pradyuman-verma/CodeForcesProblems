def ans(n, k):
    a_z = '0abcdefghijklmnopqrstuvwxyz'
    tmp = n // k
    xx = n - (tmp * k)
    ans = ''
    for i in range(1, k + 1):
        ans += a_z[i] * tmp
    if(xx):
        ans += a_z[1] * xx
    return(ans) 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        nk = list(map(int, input().strip().split()))
        print(ans(nk[0], nk[1]))