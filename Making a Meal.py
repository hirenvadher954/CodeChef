for _ in range(int(input())):
    n = int(input())
    chars = []
    for i in range(n):
        chars.extend(list(input()))
       
    c = chars.count('c')
    o = chars.count('o')
    d = chars.count('d')
    e = chars.count('e')
    h = chars.count('h')
    f = chars.count('f')
    c = c//2
    e = e//2
    
    print(min(c,o,d,e,h,f))
        
