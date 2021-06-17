def ans(h1m1,h2m2):
    h1, m1 = int(h1m1[0]), int(h1m1[1])
    h2, m2 = int(h2m2[0]), int(h2m2[1])
    cnt = 0
    for _ in range(h1, h2):
        cnt += 60
    cnt += m2 - m1
    cnt = cnt // 2
    h0 = cnt // 60
    m0 = cnt - (h0 * 60)
    h0 += h1
    m0 += m1
    if(m0 >= 60):
        h0 += m0 // 60
        m0 = m0 - (m0 // 60)*60
    h0 , m0 = str(h0), str(m0)
    if(len(h0) == 1):
        h0 = '0' + h0
    if(len(m0) == 1):
        m0 = '0' + m0
    return(h0 + ':' + m0)
if __name__ == '__main__':
    h1m1 = input().split(':')
    h2m2 = input().split(':')
    print(ans(h1m1, h2m2))