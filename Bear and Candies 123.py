# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    limak=0
    bob=0
    k=3
    for i in range(1,100000):
        if(i%2==0):
            bob=bob+i
            if bob>b:
                k=0
                break
        else:
            limak=limak+i
            if(limak>a):
                k=1
                break
    if(k==1):
        print('Bob')
    if(k==0):
        print('Limak')
            
