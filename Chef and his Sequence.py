for _ in range(int(input())):
    a = int(input())
    l = list(map(int,input().split()))
    b = int(input())
    m = list(map(int,input().split()))
    c = 0
    for i in range(a):
        if c==b:
            break
        elif m[c] == l[i]:
            c += 1
            
    if(c==b):
        print("Yes")
    else:
        print("No")        
  
