for _ in range(int(input())):
    s = input()
    flag = 0 
    for i in range(0,len(s)-1,2):
        if (s[i] == 'A' and s[i+1] =='B') or (s[i] =='B'  and s[i+1] == 'A'):
            flag = 0
        else:
            flag=1
            break
    print('no') if flag ==1 else print('yes')    
        
        
