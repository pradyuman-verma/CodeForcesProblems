def ans(arr):
    a, b, k = arr[0], arr[1], arr[2]
    net = a - b
    jump = k // 2
    if(k % 2 == 0):
        return(net * jump)
    else:
        return(net * jump + a)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = list(map(int, input().strip().split()))
        print(ans(n))