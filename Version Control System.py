t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count1 = count2 =  0 
    temp = list(range(1,n+1))
    
    for i in range(len(a)):
        if a[i] in b:
            count1 += 1
    for val in temp:
        if val not in a:
            if val not in b:
                count2 += 1
    
    print(count1,end=" ")
    print(count2)
            
    
