for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    temp = []
    for i in range(n):
        c= 0
        for j in range(i+1,n):
            if l[i]<l[j]:
                c += 1
        temp.append(c)
    print(*temp)    
    
