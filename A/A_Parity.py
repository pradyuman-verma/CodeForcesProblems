def ans(a, bk):
    b, k = bk[0], bk[1]
    if(b % 2):
        o_cnt = 0
        for i in range(0, k - 1):
            if(a[i] % 2):
                o_cnt += 1
        if(a[-1] % 2):
            o_cnt += 1
        if(o_cnt % 2):
            return('odd')
        return('even')
    else:
        if(a[-1] % 2):
            return('odd')
        return('even')
if __name__ == '__main__':
    bk = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    print(ans(a, bk))