import math
t = int(input())
for i in range(t):
    r = int(input())
    c1, c2 = list(map(int, input().split()))
    s1, s2 = list(map(int, input().split()))
    t1, t2 = list(map(int, input().split()))

    d1 = math.sqrt(((c1 - t1) ** 2) + ((c2 - t2) ** 2))
    d2 = math.sqrt(((c1 - s1) ** 2) + ((c2 - s2) ** 2))
    d3 = math.sqrt(((s1 - t1) ** 2) + ((s2 - t2) ** 2))

    if(d1 <= r or (d2 <= r and d3 <= r)):
        print("yes")
    else:
        print("no")
