t = int(input())

for i in range(t):
    count = int(input())
    su = 0
    if(count == 1):
        print("1")
    for i in range(1, count):
        su += i
        if(su == count):
            print(i)
            break
        elif(su > count):
            print(i-1)
            break
