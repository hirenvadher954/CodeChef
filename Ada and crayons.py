for _ in range(int(input())):
    s = input()
    s1 = s.replace("U"," ")
    s2 = s.replace("D"," ")
    count1 = len(s1.split())
    count2 = len(s2.split())
    print(min(count1,count2))
