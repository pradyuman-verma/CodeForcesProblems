

#import sys
import math
#import bisect
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
#from bisect import bisect_left as bl,bisect_right as br

#sys.setrecursionlimit(100000000)

inp    = lambda: int(input())
strng  = lambda: input().strip()
jn     = lambda x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
mul    = lambda: map(int,input().strip().split())
mulf   = lambda: map(float,input().strip().split())
seq    = lambda: list(map(int,input().strip().split()))

#to find mex 
def mex(arr):
    nList = set(arr)
    mex = 0
    while mex in nList:
        mex += 1
    return(mex)

def results(a):
    x, y, z, t1, t2, t3 = a[0], a[1], a[2], a[3], a[4], a[5]
    bylift = (abs(z - x) + abs(x - y)) * t2 + (3 * t3)
    bystair = abs(x - y) * t1
    if(bylift <= bystair):
        return('YES')
    return('NO')
def main():
    a = seq()
    result = results(a)
    print(result)

if __name__ == '__main__':
    main()