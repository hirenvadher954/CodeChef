t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    temp = l[:]
    for i in range(len(l)):
        if temp.count(l[i]) > 1:
            n -=1
            temp.remove(l[i])
    print(n)        
