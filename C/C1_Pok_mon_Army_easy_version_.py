
#import sys
# import math
# import bisect
# import collections
# import itertools
# from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
# from collections import defaultdict as dd, Counter as ctr
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import permutations as pr, combinations as cb

#sys.setrecursionlimit(100000000)

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())
# strng  = lambda: input().strip()
# jn     = lambda  x,l: x.join(map(str,l))
# strl   = lambda: list(input().strip())
# mul    = lambda: map(int,input().strip().split())
# mulf   = lambda: map(float,input().strip().split())
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

def find(arr, x, i):
    min_ = arr[i]
    while arr[i] != x:
        min_ = min(min_, arr[i])
        i += 1
    return(min_)
def results(arr, n):
    if(n <= 3):
        return(n)
    tmp = sorted(arr, reverse =True)
    xx = tmp[:3]
    a = tmp[0]
    b = tmp[1]
    c = tmp[2]
    i = 0
    while i < n - 1:
        if(arr[i] < arr[i + 1]):
            i += 1
            continue
        if(arr[i] in xx):
            if(arr[i] == a):
                if(arr[i + 1] != b):
                    ans = find(arr, b, i + 1)
                    return(a + b - ans)
                else:
                    ans = find(arr, c, i + 1)
                    return(a + c - ans)
            elif(arr[i] == b):
                if(arr[i + 1] != a):
                    ans = find(arr, a, i + 1)
                    return(a + b - ans)
                else:
                    ans = find(arr, b, i + 1)
                    return(b + c - ans)
            elif(arr[i] == c):
                if(arr[i + 1] != a):
                    ans = find(arr, a, i + 1)
                    return(a + c - ans)
                else:
                    ans = find(arr, b, i + 1)
                    return(b + c - ans)
        i += 1

def main():
    t = inp()
    for _ in range(t):
        nq = seq()
        n = nq[0]
        a = seq()
        result = results(a, n)
        print(result)

if __name__ == '__main__':
    main()