
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

def results(a, b, c):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]
    if(cx < ax and cy < ay and bx < ax and by < ay):
        return('YES')
    elif(cx > ax and cy > ay and bx > ax and by > ay):
        return('YES')
    elif(cx < ax and cy > ay and bx < ax and by > ay):
        return('YES')
    elif(cx > ax and cy < ay and bx > ax and by < ay):
        return('YES')
    return 'NO'

def main():
    n = inp()
    a = seq()
    b = seq()
    c = seq()
    print(results(a, b, c))

if __name__ == '__main__':
    main()