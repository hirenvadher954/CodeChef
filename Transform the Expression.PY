t = int(input())


for _ in range(t):
    string = input()
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i.isalnum():
            print(i,end="")
        elif i == ')':
            while stack[-1] != '(':
                x = stack.pop()
                print(x,end='')
            stack.pop()    
        else:
            stack.append(i)
    print()
            
