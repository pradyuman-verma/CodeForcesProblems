def ans(arr, n):
    cnt = 0
    temp = ['.' * (n + 2)]
    for i in range(n):
        temp += ['.' + ''.join(arr[i]) + '.']
    temp.append('.' * (n + 2))
    for i in range(1, n + 2):
        for j in range(1, n + 2):
            if(temp[i][j] == 'X'):
                if(temp[i - 1][j - 1] == temp[i - 1][j + 1] == temp[i + 1][j - 1] == temp[i + 1][j + 1] == 'X'):
                    cnt += 1
    return cnt
if __name__ == '__main__':
    t = int(input())
    temp = []
    for _ in range(t):
        temp.append([input()])
    print(ans(temp, t))