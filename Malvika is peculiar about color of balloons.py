t = int(input())

for _ in range(t):
    c = input()
    a = c.count('a')
    b = c.count('b')
    print(min(a,b))
