def ans(n):
    cnt = n // 7 + 1
    return(cnt)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ans(n))