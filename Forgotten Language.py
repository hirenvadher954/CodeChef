t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    word_list = input().split()
    word = []
    for l in range(k):
        word.extend(input().split())
    for ch in word_list:
        if(ch in word):
            print('YES',end=" ")
        else:
            print('NO',end=" ")
       
print()    

    
