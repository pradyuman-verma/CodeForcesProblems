
#import sys
import math
import bisect
import collections
import itertools
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, Counter as ctr
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations as pr, combinations as cb

#sys.setrecursionlimit(100000000)

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())
strng  = lambda: input().strip()
jn     = lambda  x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
mul    = lambda: map(int,input().strip().split())
mulf   = lambda: map(float,input().strip().split())
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

def results(p, n, q, m):
    e1, e2, o1, o2 = 0, 0, 0, 0
    for i in range(0, n):
        if(p[i] & 1):
            o1 += 1
        else:
            e1 += 1
    for i in range(0, m):
        if(q[i] & 1):
            o2 += 1
        else:
            e2 += 1
    return(e1 * e2 + o1 * o2)

def main():
    t = inp()
    for _ in range(t):
        n = inp()
        p = seq()
        m = inp()
        q = seq()
        result = results(p, n, q, m)
        print(result)

if __name__ == '__main__':
    main()