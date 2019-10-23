t = int(input())

for i in range(t):
    a = int(input())
    count = 0
    if a%5 == 0:
        while(a%10!=0):
            a = a*2
            count += 1
        print(count)    
    else:
        print("-1")
