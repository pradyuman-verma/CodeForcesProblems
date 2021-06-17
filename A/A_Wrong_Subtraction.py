def ans(n, k):
    while k > 0:
        if(n % 10 == 0):
            n = n // 10
        else:
            n -= 1
        k -= 1
    return n

if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    print(ans(nk[0], nk[1]))