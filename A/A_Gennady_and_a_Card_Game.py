def ans(s, t):
    for i in t:
        if(i[0] == s[0] or i[1] == s[1]):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    s = input()
    t = input().strip().split()
    print(ans(s, t))
    