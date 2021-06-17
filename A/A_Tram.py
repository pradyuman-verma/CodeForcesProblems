def ans(arr):
    cnt = 0
    summ = 0
    for [i,j] in arr:
        cnt += (j - i)
        summ = max(summ, cnt)
    return summ

if __name__ == '__main__':
    n = int(input())
    temp = [[0, 0]]
    for _ in range(n):
        temp.append(list(map(int, input().strip().split())))
    print(ans(temp))