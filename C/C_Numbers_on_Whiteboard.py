from math import ceil
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())
# strng  = lambda: input().strip()
# jn     = lambda  x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
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

def results(n):
    print(2)
    j = n
    for i in range(n - 1, 0, -1):
        print('{} {}'.format(j, i))
        j = ceil((j + i) / 2)
def main():
    t = inp()
    for _ in range(t):
        n = inp()
        results(n)

if __name__ == '__main__':
    main()