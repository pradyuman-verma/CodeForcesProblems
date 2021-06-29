
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())

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

def results(p, q):
    p1, p2, p3 = p[0], p[1], p[2]
    q1, q2, q3 = q[0], q[1], q[2]
    return(min(p1, q2) + min(p2, q3) + min(p3, q1))

def mii(p, q, n):
    p1, p2, p3 = p[0], p[1], p[2]
    q1, q2, q3 = q[0], q[1], q[2]
    return(max(p1 + q2 - n, p2 + q3 - n, p3 + q1 - n, 0))   

def main():
    n = inp()
    a = seq()
    b = seq()
    x = results(a, b)
    z = mii(a, b, n)
    print("{} {}".format(z, x))

if __name__ == '__main__':
    main()