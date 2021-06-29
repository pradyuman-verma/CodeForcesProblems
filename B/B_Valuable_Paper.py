
#import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
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

def results(a, n, m):
    if(m < n):
        return(-1)
    else:
        a.sort()
        tmp = dd(set)
        fac = set()
        port = set()
        for arr in a:
            min_ = min(arr[0], arr[1])
            # max_ = max(arr[0], arr[1])
            fac.add(arr[1])
            port.add(arr[0])
            if(min_ not in tmp.keys()):
                tmp[min_].add(arr[2])
            else:
                tmp[min_].add(min(arr[2], min(tmp[min_])))
        maxx = [0] * (n + 1)
        if(len(fac) < n or len(port) < n):
            return(-1)
        for x in tmp.keys():
            maxx[x] = min(tmp[x])
    return(max(maxx))
def main():
    nm = seq()
    n, m = nm[0], nm[1]
    a = []
    for _ in range(m):
        a.append(seq())
    print(results(a, n, m))

if __name__ == '__main__':
    main()