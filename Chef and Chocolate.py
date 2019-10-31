for _ in range(int(input())):
    l = list(map(int,input().split()))
    
    if l[0]*l[1]%2 == 0:
        print("Yes")
    else:
        print("No")
    
