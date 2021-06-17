def ans(w):
    temp = w[0].upper() + w[1:]
    return(temp)

if __name__ == '__main__':
    w = input()
    print(ans(w))