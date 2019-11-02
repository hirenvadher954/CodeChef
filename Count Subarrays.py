for _ in range(int(input())):
	n = int(input())
	li = list(map(int, input().split()))
	li1 = [1]*n
	for i in range(1,n):
	    if li[i]>=li[i-1]:
	        li1[i] += li1[i-1]
	print(sum(li1))        
