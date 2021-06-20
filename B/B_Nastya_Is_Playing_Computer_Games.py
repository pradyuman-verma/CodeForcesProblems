def ans(n, k):
    if(n == 2):
        return(6)
    return(min(k - 1, n - k) + 6 + 3 *(n - 2))

if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    print(ans(nk[0], nk[1]))