t = int(input())

for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    
    for val in l:
        if (not l.count(val)%2 == 0):
            print(val)
            break
