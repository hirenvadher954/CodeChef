for _ in range(int(input())):
    c,d,n = map(int,input().split())
    
    for i in range(n):
        if i%2 == 0:
            c *= 2
        else:
            d *= 2
    
     
    
    print(max(c,d)//min(c,d))
        
    
