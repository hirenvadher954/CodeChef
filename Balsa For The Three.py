for _ in range(int(input())):
    a = int(input()) + 1
    while str(a).count('3')<3:
        a +=1
    print(a)    
