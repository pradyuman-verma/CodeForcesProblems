
#import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
# from collections import Counter as ctr
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import permutations as pr, combinations as cb

#sys.setrecursionlimit(100000000)

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
inp    = lambda: int(input())
seq    = lambda: list(map(int,input().strip().split()))
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

# p_inf = float('inf')
# n_inf = float('-inf')
#To find mex 
# def mex(arr):
#     nList = set(arr)
#     mex = 0
#     while mex in nList:
#         mex += 1
#     return(mex)

def results(arr, n, k):
    arr = '0' + arr + '0'
    ll, ans, summ = 0, 0, 0
    dummy = []
    loop = True
    for i in range(1, n + 1):
        if(arr[i] == 'L'):
            ll += 1
            if(loop):
                j = i
                loop = False
            if(arr[i + 1] == 'W' or arr[i + 1] == '0'):
                dummy.append(i - j + 1)
                loop = True
        else: 
            ans += 1
            if(arr[i - 1] == 'W'):
                ans += 1
    if(dummy == [] or k == 0):
        return(ans)
    if(k >= ll):
        return(1 + (n - 1) * 2)
    n = len(dummy)
    dummy.sort()
    ll = 0
    for i in range(n):
        if(summ + dummy[i] <= k):
            summ += dummy[i]
            ll += 1
        else:
            break
    k -= summ
    ans += summ * 2 + ll + k * 2
    return(ans)

def main():
    t = inp()
    for _ in range(t):
        nk = seq()
        n, k = nk[0], nk[1]
        a = input()
        result = results(a, n, k)
        print(result)

if __name__ == '__main__':
    main()