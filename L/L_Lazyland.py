from collections import defaultdict
def ans(a, b):
    tmp = defaultdict(list)
    for i in range(0, n):
        tmp[a[i]].append(i)
    if(len(tmp.keys()) == k):
        return 0 
    length = k - len(tmp.keys())
    dmp = []
    for i in tmp.keys():
        if(len(tmp[i]) > 1):
            dmp.append(tmp[i])
    cnt = 0
    temp = []
    for i in dmp:
        max_ = []
        for j in i:
            max_.append([b[j], j])
        max_.sort(reverse=True)
        max_.pop(0)
        temp += max_[::]
    temp.sort()
    temp = temp[:length]
    for i in temp:
        cnt += i[0]
    return(cnt)
if __name__ == '__main__':
    nk = list(map(int, input().strip().split()))
    n, k = nk[0], nk[1]
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    print(ans(a, b))