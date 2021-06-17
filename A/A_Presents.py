def ans(arr):
    temp = [0] * (n + 1)
    for i in range(n):
        temp[arr[i]] = i + 1
    return(temp[1:])

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().strip().split()))
    print(*ans(p))