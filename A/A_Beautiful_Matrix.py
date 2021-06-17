def ans(arr):
    i, j = 0, 0
    for x in range(5):
        if(1 in arr[x]):
            i = x
            for y in range(5):
                if(arr[i][y] == 1):
                    j = y
                    break
            break
    return(abs(i - 2) + abs(j - 2))

if __name__ == '__main__':
    t = 5
    temp = []
    for _ in range(t):
        temp.append(list(map(int, input().strip().split())))
    print(ans(temp))