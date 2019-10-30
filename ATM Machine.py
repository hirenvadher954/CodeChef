for _ in range(int(input())):
    t,n = map(int,input().split())
    l = list(map(int,input().split()))
    m = []
    for val in l:
        if val <= n:
            n -= val
            m.append(1)
        else:
            m.append(0)
            
    d = ''.join(str(i) for i in m)
    print(d)
