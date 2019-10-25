s = input()

for i in range(int(input())):
    d = input()
    flag = 1
    
    for word in d:
        if word not in s:
            print('No')
            flag = 0
            break
    if flag == 1:
        print("Yes")
