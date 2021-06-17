def ans(arr):
    if(n == 0):
        return(l // a)
    cnt = 0
    num = 0
    for x in range(0, n):
        cnt += (arr[x][0] - num) // a
        num = arr[x][0] + arr[x][1]
    cnt += (l - num) // a
    return(cnt)

if __name__ == '__main__':
    nla = list(map(int, input().strip().split()))
    n, l, a = nla[0], nla[1], nla[2]
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().strip().split())))
    print(ans(temp))