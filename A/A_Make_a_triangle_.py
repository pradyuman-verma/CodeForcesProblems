def ans(arr):
    arr.sort()
    a, b, c = arr[0], arr[1], arr[2]
    if(a + b > c):
        return(0)
    cnt = 0
    while a + b <= c:
        a += 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    abc = list(map(int, input().strip().split()))
    print(ans(abc))