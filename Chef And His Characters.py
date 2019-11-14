for _ in range(int(input())):
    s = input()
    count=0
    for i in range(len(s)):
        if set(s[i:i+4]) == set('chef'):
            count += 1
    if count>0:
        print("lovely",count)
    else:
        print('normal')
