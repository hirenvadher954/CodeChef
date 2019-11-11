for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    
    while len(l) != 2:
        arr1=l[:3]
        arr1.sort()
        l.remove(arr1[1])
    print(*l)    
