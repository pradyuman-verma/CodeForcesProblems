
#import sys
import math
import bisect
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, Counter as ctr
from bisect import bisect_left as bl, bisect_right as br

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

#To find mex 
def mex(arr):
    nList = set(arr)
    mex = 0
    while mex in nList:
        mex += 1
    return(mex)

def results(arr, n):
    arr.sort()
    min_, max_ = arr[0], arr[-1]
    return max_ - min_ - n + 1

def main():
    n = inp()
    a = seq()
    result = results(a, n)
    print(result)

if __name__ == '__main__':
    main()