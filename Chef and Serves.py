for _ in range(int(input())):
    n1,n2,k = map(int,input().split())
    
    if (n1+n2)%(2*k)<k:
        print("CHEF")
    else:
        print("COOK")
