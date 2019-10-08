t = int(input())

for i in range(t):
    n = int(input())
    string = str(input())
    M=0
    if 'Y' in string:
        print("NOT INDIAN")
        M=1
        
    if 'I' in string:
        print("INDIAN")
        M=1
    elif(M==0):
        print("NOT SURE")
