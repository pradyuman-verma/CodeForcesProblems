
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

def results(c, nab):
    n, a, b = nab[0], nab[1], nab[2]
    x = min(a, b)
    cnt = 0
    if(n % 2):
        if(c[n // 2] == 2):
            cnt += x
    for j, i in enumerate(range(0, n // 2), 1):
        if(c[i] == c[-j]):
            if(c[i] == 2):
                cnt += x * 2
        elif (c[i] == 1 and c[-j] == 2) or (c[i] == 2 and c[-j] == 1):
            cnt += b
        elif(c[i] == 0 and c[-j] == 2) or (c[i] == 2 and c[-j] == 0):
            cnt += a
        else:
            return(-1)
    return cnt

def main():
    nab = seq()
    c = seq()
    result = results(c, nab)
    print(result)

if __name__ == '__main__':
    main()