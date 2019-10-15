# cook your dish here


n,k = map(int,input().split())

l = [0]*n
for i in range(k):
	s = input()
	if "CLOSEALL" in s:
		l = [0]*n
	else:
		x,t = map(str,s.split())	
		if l[int(t)-1] == 0:
			l[int(t)-1] = 1
		else:
			l[int(t)-1] = 0	
	print(l.count(1))	


