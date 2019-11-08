for _ in range(int(input())):
    s = input()
    count=0
    for i in range(len(s)-1):
        if s[i] == '<' and s[i+1] == '>':
            count += 1
    print(count)        
