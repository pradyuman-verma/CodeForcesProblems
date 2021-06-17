def ans(n):
    sum_ = n * (n + 1)
    sum_ = sum_ // 2
    if(sum_ % 2):
        return(1)
    return(0)
if __name__ == '__main__':
    n = int(input())
    print(ans(n))
    