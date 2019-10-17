t= int(input())

for _ in range(t):
    str1 = input()
    str2 = input()
    minimum=maximun=0
    for i in range(len(str1)):
        if str1[i]=='?' or str2[i]=='?':
            maximun += 1
        else:
            if str1[i]!=str2[i]:
                minimum += 1
                maximun += 1
    print(minimum,maximun)            
