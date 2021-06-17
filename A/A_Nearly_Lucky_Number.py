def ans(arr):
    cnt = arr.count('4') + arr.count('7')
    if(cnt == 4 or cnt == 7):
        return('YES')
    return('NO')

if __name__ == '__main__':
    n = list(input())
    print(ans(n))
    