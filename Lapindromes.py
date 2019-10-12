n = int(input())

for i in range(n):
    text = list(input())
    mid = len(text)//2
   
    l=[]
    count=0
    for j in range(mid):
        l.append(text[j])

    if(len(text)%2==0):
        mid=mid
    else:
        mid=mid+1    
    
    for char in text[mid:]:
        if char in l:
            count+=1
            l.remove(char)
    
    if(len(text)%2==1):
        mid-=1
            
    if(count==mid):
        print("YES")
    else:
        print("NO")    
        
