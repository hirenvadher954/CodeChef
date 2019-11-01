for _ in range(int(input())):
    t = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    
    if t!=1: 
        l.remove(max(l))
        r.remove(max(r))
  
    if sum(l)<sum(r):
        print("Alice")
    elif sum(l)>sum(r):
        print("Bob")
    else:
        print('Draw')
        
