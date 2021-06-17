def ans(a, b):
    if(sum(a[:s]) == s):
        return('YES')
    if(a[0] == 0):
        return('NO')
    if(a[s - 1] == 1):
        return('YES')
    elif((a[s - 1] == 0 and b[s - 1] == 0)):
        return('NO')
    elif((a[s - 1] == 0 and b[s - 1] == 1) or (a[s - 1] == 1 and b[s - 1] == 0)):
        for i in range(s, n):
            if(a[i] == 1 and b[i] == 1):
                return('YES')
        return('NO')
    return('YES')

if __name__ == '__main__':
    ns = list(map(int, input().strip().split()))
    n, s = ns[0], ns[1]
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    print(ans(a, b))