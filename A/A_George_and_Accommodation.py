def ans(arr):
    cnt = 0
    for [i, j] in arr:
        if(j - i >= 2):
            cnt += 1
    return cnt

if __name__ == '__main__':
    t = int(input())
    temp = []
    for _ in range(t):
        temp.append(list(map(int, input().strip().split())))
    print(ans(temp))