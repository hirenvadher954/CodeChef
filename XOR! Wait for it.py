
for _ in range(int(input())):
    l,r=[int(x) for x in input().split()]
    o=(r-l)//2
    if r%2!=0 or l%2!=0:
        o+=1
    if o%2==0:
        print("Even")
    else:
        print("Odd")
