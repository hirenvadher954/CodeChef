for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=0
    b=0
    h=list(filter(lambda x:a.count(x)>=2,a))
    s=list(set(h))
    s.sort(reverse=True)
    if(a.count(s[0])>=4):
        print(s[0]**2)
    elif(len(s)>=2):
        print(s[0]*s[1])
    else:
        print(-1)
