def ans(arr):
    i = 1
    a = arr[0]
    while i < n:
        b = arr[i]
        a = a.intersection(b)
        i += 1
    return sorted(list(a))

if __name__ == '__main__':
    n = int(input())
    temp = []
    for _ in range(n):
        r = list(map(int, input().strip().split()))
        temp.append(set(r[1:]))
    print(*ans(temp))