for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = l[0:]
    l.reverse()
    
    def find_missing(lst): 
        return sorted(set(range(1,8)) - set(lst))
    
    if (l == d):
        t = find_missing(l)
        if len(t)==0:
            print('yes')
        else:
            print('no')
    else:
        print('no')
