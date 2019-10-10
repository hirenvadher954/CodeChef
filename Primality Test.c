t = int(input())

for i in range(t):
    a = int(input())
    flag=0
    for i in range(2,a//2):
        if a%i == 0:
            flag=1
    
    if flag==0:
        print("yes")
    else:
        print("no")    
