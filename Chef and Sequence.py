for _ in range(int(input())):
    x,y=map(int,input().split())
    s=list(map(int,input().split()))
    j=s.count(1)
    if x-j>y:
        print('NO')
    else:
        print('YES')
