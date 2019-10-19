t = int(input())


for _ in range(t):
    a = int(input())
    b = map(int,input().split())
    a = a-1
    print(min(b)*a)
