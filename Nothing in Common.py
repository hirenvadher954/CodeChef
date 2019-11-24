for _ in range(int(input())):
    a,b = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    for val in a:
        if val in b:
            count += 1
    print(count)        
