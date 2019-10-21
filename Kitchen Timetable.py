t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    if a[0] >= b[0]:
        count+=1
    for i in range(len(a)-1):
        if a[i+1]-a[i] >= b[i+1]:
            count+=1
    
    print(count)
