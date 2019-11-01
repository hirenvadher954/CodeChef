for _ in range(int(input())):
    t = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    temp = [a*b for a,b in zip(l,r)]
    tempMax = max(temp)
    if temp.count(tempMax) > 1:
        rindex = r.index(max(r))
        print(rindex+1)
        
    else:
        print(temp.index(tempMax)+1)
