
# #import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
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

def results(a, b, c, n):
    temp = [a[0]]
    for i in range(1, n - 1):
        if(a[i] != temp[i - 1]):
            temp.append(a[i])
        elif(b[i] != temp[i - 1]):
            temp.append(b[i])
        else:
            temp.append(c[i])
    if(a[n - 1] != temp[0] and a[n - 1] != temp[-1]):
        temp.append(a[n - 1])
    elif(b[n - 1] != temp[0] and b[n - 1] != temp[-1]):
        temp.append(b[n - 1])
    else:
        temp.append(c[n - 1])
    return(temp)

def main():
    t = inp()
    for _ in range(t):
        n = inp()
        a = seq()
        b = seq()
        c = seq()
        result = results(a,b,c,n)
        print(*result)

if __name__ == '__main__':
    main()