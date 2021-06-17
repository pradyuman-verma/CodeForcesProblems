def ans(n, k):
    r, g, b = n * 2, n * 5, n * 8
    cnt = 0
    if(r % k):
        cnt += r // k + 1
    else:
        cnt += r // k
    if(g % k):
        cnt += g // k + 1
    else:
        cnt += g // k
    if(b % k):
        cnt += b // k + 1
    else:
        cnt += b // k
    return cnt

if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    n, k = nk[0], nk[1]
    print(ans(n, k))