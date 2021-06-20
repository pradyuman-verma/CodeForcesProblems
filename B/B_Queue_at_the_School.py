def ans(arr, t):
    while(t):
        i = 0
        while i < n - 1:
            if(arr[i] == 'B' and arr[i + 1] == 'G'):
                arr[i], arr[i + 1] = 'G', 'B'
                i += 1
            i += 1
        t -= 1
    return arr

if __name__ == '__main__':
    nt = list(map(int, input().strip().split()))
    n, t= nt[0], nt[1]
    s = list(input())
    print(''.join(ans(s, t)))
        