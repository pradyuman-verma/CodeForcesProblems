def ans(arr):
    n, s = arr[0], arr[1]
    if(s > n):
        if(s % n):
            return(s // n + 1)
        else:
            return(s // n)
    elif(s <= n):
        return(1)

if __name__ == '__main__':
    n = list(map(int, input().strip().split()))
    print(ans(n))