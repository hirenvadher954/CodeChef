t = int(input())

for i in range(t):
    m,n,k = map(int,input().split())
    diff = abs(m-n)
    if(diff>k):
        if m<n:
            m += k
        else:
            n += k
        print(abs(m-n))    
    
    else:
        print("0")
