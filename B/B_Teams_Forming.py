from collections import  Counter
def ans(arr):
    arr.sort()
    temp = dict(Counter(arr))
    cnt = 0 
    tmp = list(temp.keys())
    for i in range(len(tmp) - 1):
        if(temp[tmp[i]] % 2):
            cnt += abs(tmp[i + 1] - tmp[i])
            temp[tmp[i + 1]] += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))