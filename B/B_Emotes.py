def ans(arr):
    arr.sort(reverse = True)
    x = m // (k + 1)
    cnt = arr[0] * k + arr[1]
    cnt *= x
    x = m - (x * (k + 1))
    if(x <= k):
        cnt += arr[0] * x
    return cnt

if __name__ == '__main__':
    nmk = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    n, m, k = nmk[0], nmk[1], nmk[2]
    print(ans(a))