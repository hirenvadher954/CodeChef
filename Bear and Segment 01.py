for _ in range(int(input())):
    s = list(input())
    d = s.count('1')
    count = 0
    for i in range(len(s)-1):
        if s[i] == '1' and s[i+1] == '1':
            count += 1

    if d-1 == count:
        print("YES")
    else:
        print("NO")
        
