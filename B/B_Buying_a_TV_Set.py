
#import sys
import math
import bisect
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, Counter as ctr
from bisect import bisect_left as bl,bisect_right as br

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

def results(arr):
    a, b, x, y = arr[0], arr[1], arr[2], arr[3]
    g = gcd(x, y)
    w, h = x // g, y // g
    return min(a // w, b // h)

def main():
    a = seq()
    result = results(a)
    print(result)

if __name__ == '__main__':
    main()