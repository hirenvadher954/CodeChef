t = int(input())

for _ in range(t):
        price,quantity = list(map(float,input().split()))
        
        if(price>1000):
            price-=price*0.1
        
        print("{0:.6f}".format(price*quantity))
        
