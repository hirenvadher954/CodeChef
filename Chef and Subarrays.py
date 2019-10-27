from  numpy import prod
t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    t=0
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(s[i:j]) == prod(s[i:j]):
                t += 1
    print(t)            
