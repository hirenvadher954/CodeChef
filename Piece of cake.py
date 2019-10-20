t = int(input())

for _ in range(t):
    a = input()
    flag=0
    length  = len(a)/2
    for i in a:
        if a.count(i) == length:
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
    
