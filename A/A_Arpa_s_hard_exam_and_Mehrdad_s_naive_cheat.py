def ans(t):
    if(t == 0):
        return(1)
    tmp = [6 ,8, 4, 2]
    t = t % 4
    return tmp[t]

if __name__ == '__main__':
    t = int(input())
    print(ans(t))