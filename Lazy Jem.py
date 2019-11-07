import math
for _ in range(int(input())):
    N,Break,Minutes = map(int,input().split())
    tempM=0
    while N>0:
        x = math.ceil(N/2)
        tempM  = tempM + x*Minutes + Break
        Minutes = Minutes*2
        N -= x
    print(tempM-Break)    
