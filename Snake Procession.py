for _ in range(int(input())):
    n = int(input())
    l = input()
    temp = []
    for val in l:
        if val != '.':
            temp.append(val)
    if len(temp)==0:
        print('Valid')
    elif len(temp)%2==1:
        print('Invalid')    
    else:
        flag=0
        for i in range(0,len(temp)-1,2):
            if temp[i] == 'H' and temp[i+1] == 'T':
                flag=1
            else:
                flag=0
                break
        if flag==1:
            print('Valid')
        else:
            print('Invalid')    
