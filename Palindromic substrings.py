for _ in range(int(input())):
    a = input()
    b = input()
    flag = 0
    for text in a:
        if text in b:
            print("Yes")
            flag=1
            break
    if flag == 0:
        print("No")
