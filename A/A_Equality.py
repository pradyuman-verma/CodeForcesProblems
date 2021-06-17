
#import sys
import math
import bisect
import collections
import itertools
import string
#from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, Counter as ctr
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations as pr, combinations as cb
from string import ascii_uppercase as a_up
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
p_inf = float('inf')
n_inf = float('-inf')
#To find mex 
def mex(arr):
    nList = set(arr)
    mex = 0
    while mex in nList:
        mex += 1
    return(mex)

def results(arr, k):
    tmp = ctr(arr)
    aplha = list(a_up[ : k])
    cnt = p_inf
    for i in aplha:
        try:
            cnt = min(tmp[i], cnt)
        except:
            return(0)
    return cnt * k

def main():
    nk = seq()
    n, k = nk[0], nk[1]
    s = strl()
    print(results(s, k))

if __name__ == '__main__':
    main()