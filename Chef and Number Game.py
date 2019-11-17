

for i in range (int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    m=0
    for j in b:
        if j<0:
            m=m+1
            
            
            
    if(m>0):
        print(max(m,n-m), min(m,n-m))
    
    else:
        print(max(m,n-m), max(m,n-m))
        
        
        
        
