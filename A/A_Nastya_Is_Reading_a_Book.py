def ans(arr):
    cnt = 0
    for i in range(n):
        if(k >= arr[i][0] and k <= arr[i][1]):
            break
        cnt += 1
    return(n - cnt)

if __name__ == '__main__':
    n = int(input())
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().strip().split())))
    k = int(input())
    print(ans(temp))