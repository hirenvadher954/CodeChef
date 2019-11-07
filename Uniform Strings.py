for _ in range(int(input())):
    s = input()
    count=0
    for i in range(len(s)-1):
        if s[i] == '0' and s[i+1] == '1':
            count += 1
        elif s[i] == '1' and s[i+1] == '0':
            count += 1
    if count > 2:
        print('non-uniform')
    else:
        print('uniform')
