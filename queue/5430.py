T = int(input())

for i in range(T):
    p = input()
    n = int(input())

    de = input()[1:-1].split(',')
    p = p.replace('RR', '')

    r, f, b = 0, 0, 0

    for j in p:
        if j == 'R':
            r+=1
        elif j == 'D':
            if r%2 == 0:
                f += 1
            else:
                b += 1
    
    if f + b <= n:
        de = de[f:n-b]

        if r%2 == 1:
            print('['+','.join(de[::-1]) + ']')
        else:
            print('[' + ','.join(de) + ']')
    
    else:
        print('error')