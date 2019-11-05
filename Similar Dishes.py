for i in range(int(input())):
    a = list(map(str,input().split()))
    b = list(map(str,input().split()))
    count = 0
    flag=0
    for valA in a:
        if b.count(valA)>0:
            count += 1
            
    if count>=2:
        print('similar')
    else:
        print('dissimilar')

 
