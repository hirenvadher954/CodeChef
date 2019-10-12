t = int(input())

for _ in range(t):
        a = int(input())
        b = list(map(int,input().split()))
        min=b[0]+b[1]
        
        for i in range(a):
            for j in range(a):
                if(i!=j):
                    if(min>b[i]+b[j]):
                        min = b[i]+b[j]
    
    
        print(min)                    
