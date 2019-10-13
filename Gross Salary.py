t = int(input())

for i in range(t):
    bs = float(input())

    if bs<1500:
        hra = 0.1*bs 
        da = 0.9*bs

    if bs>=1500:
        hra = 500 
        da = 0.98*bs
    
    print("{0:.2f}".format(bs+hra+da))
