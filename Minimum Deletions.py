import math
for _ in range(int(input())):
    a=int(input())
    l = list(map(int,input().split()))
    first = l[0]
    for i in range(1,len(l)):
        d = math.gcd(first,l[i])
    if d==1:
        print('0')
    else:
        print('-1')
