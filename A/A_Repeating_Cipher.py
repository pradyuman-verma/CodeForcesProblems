def ans(arr, n):
    i = len(arr) - 1
    s = ''
    D = 1 + (8 * n)
    xx = -1 + (D)**(.5)
    xx = xx // 2
    i = n - 1
    while i >= 0:
        s += arr[i]
        i -= int(xx)
        xx -= 1    
    return(s[::-1])

if __name__ == '__main__':
    n = int(input())
    t = list(input())
    print(ans(t, n))