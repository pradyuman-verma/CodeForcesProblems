def ans(s):
    s = s.replace('+',' ')
    s = sorted(s.split(' '))
    return("+".join(s))

if __name__ == '__main__':
    s = input()
    print(ans(s))