def ans(x):
    if(x == 1):
        return(-1)
    return(f'{x} {x}')

if __name__ == '__main__':
    x = int(input())
    print(ans(x))