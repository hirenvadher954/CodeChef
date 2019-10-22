from collections import Counter 
t=int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    l = Counter(l)
    if list(l.values())==[2,2] or list(l.values())==[4]:
        print("YES")
    else:
        print("NO")

