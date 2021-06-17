def ans(nm):
    n = nm[0]
    m = nm[1]
    if(n < m):
        return(-1)
    elif(n == m):
        return(n)
    else:
        if(n % 2 == 0):
            move = n // 2
        else:
            move = n // 2 + 1
        if(move % m):
            move = (move // m) + 1
            move = move * m
    return(move)


if __name__ == '__main__':
    nm = list(map(int, input().strip().split()))
    print(ans(nm))