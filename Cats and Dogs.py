for _ in range(int(input())):
    c,d,n = map(int,input().split())
    
    if n%4!=0 or n<d*4 or n>(c+d)*4:
        print("no")
    else:
        if c > (2*d + (n/4 - d)):
            print('no')
        else:
            print('yes')
            
    
