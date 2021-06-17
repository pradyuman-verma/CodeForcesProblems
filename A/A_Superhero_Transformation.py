def ans(s, t):
    vow = 'aeiou'
    con = 'bcdfghjklmnpqrstvwxyz'
    s_len, t_len = len(s), len(t)
    if(s_len != t_len):
        return('No')
    for i in range(s_len):
        if((s[i] in vow) and (t[i] in vow)):
            continue
        elif((s[i] in con) and (t[i] in con)):
            continue
        else:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    s = list(input())
    t = list(input())
    print(ans(s, t))