def ans(s):
    cnt = 0
    for i in range(n):
        if(s[i] in ['2', '4', '6', '8']):
            cnt += i + 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(ans(s))