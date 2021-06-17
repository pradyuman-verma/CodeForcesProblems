def ans(l, r):
    i = l
    while i <= r:
        if(i * 2 <= r):
            return([i, i * 2])

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        lr = list(map(int, input().strip().split()))
        print(*ans(lr[0], lr[1]))