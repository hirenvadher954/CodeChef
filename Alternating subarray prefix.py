for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = [1]*n
	for i in range(n - 2, -1, -1):
		if  arr[i]*arr[i + 1] < 0:
		    ans[i] = 1 + ans[i+1]
	print(*ans)
