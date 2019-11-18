for _ in range(int(input())):
    n,x = map(int,input().split())
    s = input()
    l = []
    l.append(x)
    for val in s:
        if 'R'==val:
            x = x+1
            l.append(x)
        else:
            x -= 1
            l.append(x)
    print(len(set(l)))
