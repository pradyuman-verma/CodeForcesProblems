def ans(arr):
    k, n, w = arr[0], arr[1], arr[2]
    cnt = 0
    for i in range(1, w + 1):
        cnt += k * i
    if(n < cnt):
        return abs(n - cnt)
    else:
        return(0)

if __name__ == '__main__':
    knw = list(map(int, input().strip().split()))
    print(ans(knw))