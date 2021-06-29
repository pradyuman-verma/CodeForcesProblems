
#import sys
import math
import bisect
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

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

def results(l, r):
    for i in range(l, r, 2):
        print(i, i + 1)

def main():
    lr = seq()
    l, r = lr[0], lr[1]
    print('YES')
    results(l, r)
if __name__ == '__main__':
    main()