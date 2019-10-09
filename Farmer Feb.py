T=int(input())
while T:
    T=T-1
    x,y= map(int,input().split())
    flag=0
    sum=x+y
    for i in range(sum+1,sum+100):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
        if(flag==0):
            print(i-sum)
            break
