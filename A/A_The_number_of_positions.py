def ans(nab):
    n, a, b = nab[0], nab[1], nab[2]
    x = a + b
    if(x == n):
        return(b)
    elif(x < n):
        return(b + 1)
    else:
        return(n - a)

if __name__ == '__main__':
    nab = list(map(int, input().strip().split()))
    print(ans(nab))