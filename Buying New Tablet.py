t = int(input())
for i in range(t):
	n, b = map(int, input().split())
	area = 0
	for i in range(n):
		w, h, p = map(int, input().split())
		if b >= p:
			if area < w*h:
				area = w*h
	if area == 0:
		print("no tablet")
	else:
		print(area)
