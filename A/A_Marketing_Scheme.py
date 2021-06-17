
# import sys
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
strl   = lambda: list(input().strip())
seq    = lambda: list(map(int,input().strip().split()))
# strng  = lambda: input().strip()
# jn     = lambda  x,l: x.join(map(str,l))
# mul    = lambda: map(int,input().strip().split())
# mulf   = lambda: map(float,input().strip().split())
# pow2   = lambda x: x and not(x & (x - 1))

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

def f(arr):
    l, r = arr[0], arr[1]
    if(r < 2 * l):
        return('YES')
    return('NO')

def main():
    t = inp()
    for _ in range(t):
        a = seq()
        result =f(a)
        print(result)

if __name__ == '__main__':
    main()