t = int(input())

for _ in range(t):
    a,b,c,d = map(int,input().split())
    
    if a==c:
        if(b>d):
            print('down')
        else:
            print('up')
    elif b==d:
        if(a>c):
            print('left')
        else:
            print('right')
    else:
        print('sad')
