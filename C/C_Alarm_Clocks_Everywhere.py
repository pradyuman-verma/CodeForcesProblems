
#import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
from math import gcd
# from collections import defaultdict as dd, Counter as ctr
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import permutations as pr, combinations as cb

#sys.setrecursionlimit(100000000)

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())
# strng  = lambda: input().strip()
# jn     = lambda  x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
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

def f(x, p, m, n):
    g = x[1] - x[0]
    for i in range(1, n - 1):
        g = gcd(x[i + 1] - x[i], g)
    for i in range(m):
        if(g % p[i] == 0):
            return(['YES', [x[0], i + 1]])
    return(['NO'])

def main():
    nm = seq()
    n, m = nm[0], nm[1]
    a = seq()
    p = seq()
    result =f(a, p, m, n)
    print(result[0])
    if(len(result) > 1):
        print(*result[1])

if __name__ == '__main__':
    main()