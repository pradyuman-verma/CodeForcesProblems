def ans(a, b):
    ans = []
    d = {a[x] : x for x in range(n)}
    i = 0
    temp = 0
    for i in range(0, n):
        cnt = 0
        ind = d[b[i]] + 1
        if(ind > temp):
            cnt = ind - temp 
        temp = max(ind, temp)
        ans.append(cnt)
    return ans 

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(*ans(A, B))