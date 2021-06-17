def ans(xyz, abc):
    x, y, z = xyz[0], xyz[1], xyz[2]
    a, b, c = abc[0], abc[1], abc[2]
    if(a >= x):
        a -= x
    else:
        return('NO')
    if(a + b >= y):
        if(b >= y):
            b -= y
        else:
            y -= b
            b = 0
            a -= y
    else:
        return('NO')
    if(a + b + c >= z):
        return('YES')
    else:
        return 'NO'
if __name__ == '__main__':
    xyz = list(map(int, input().strip().split()))
    abc = list(map(int, input().strip().split()))
    print(ans(xyz, abc))