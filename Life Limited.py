for _ in range(int(input())):
    a=input()
    b=input()
    c=input()
    for i in range(2):
        if((a[i]=='l' and b[i]=='l' and b[i+1]=='l') or (b[i]=='l' and c[i]=='l'  and c[i+1]=='l')):
            print('yes')
            break
    else:
        print('no')
