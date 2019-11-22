# cook your dish here
for a0 in range(int(input())):
      array=[]
      for i in range(10):
            array.append(list(map(int, input().split())))
      count=0
      for i in array:
            for j in i:
                  if j<=30:
                        count+=1
      if count>=60:
            print("yes")
      else:
            print("no")
