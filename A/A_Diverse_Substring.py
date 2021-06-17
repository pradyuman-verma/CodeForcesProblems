def ans(s):
    i = 0
    while i < n - 1:
        if(s[i] != s[i + 1]):
            print('YES')
            return(s[i] + s[i + 1])
        i += 1
    return('NO')

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(ans(s))