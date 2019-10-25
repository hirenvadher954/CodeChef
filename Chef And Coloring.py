t = int(input())

for _ in range(t):
    a = int(input())
    l = input()
    temp = []
    r=g=b=0
    for val in l:
        temp.append(val)
    r = temp.count('R') 
    g = temp.count('G')    
    b = temp.count('B')    

    print(a-max(r,g,b))   
    
    
    
