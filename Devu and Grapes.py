for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    count = 0 
    for i in range(n):
        rem = l[i]%k
        diff = k - rem
        if l[i]>=k:
            count += min(rem,diff)
        else:
            count += diff
            
    print(count)        
    
