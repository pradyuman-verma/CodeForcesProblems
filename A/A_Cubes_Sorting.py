
#import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
#from collections import Counter as ctr
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

def results(arr, n):
    tmp = sorted(arr)
    for i in range(n - 1):
        if(tmp[i] == tmp[i + 1]):
            return('YES')
    if(arr != tmp[:: -1]):
        return('YES')
    return('NO')

def main():
    t = inp()
    for _ in range(t):
        n = inp()
        a = seq()
        result = results(a, n)
        print(result)

if __name__ == '__main__':
    main()