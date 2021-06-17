def ans(x):
    steps = x // 5
    if(x % 5):
        steps += 1
    return steps

if __name__ == '__main__':
    x = int(input())
    print(ans(x))
    