t = int(input())

for i in range(t):
    M, x, y = list(map(int, input().split()))
    cops_loc = input().split()
    l = [0]*100
    mul = x*y

    for cop in cops_loc:
        cop = int(cop)
        for i in range(cop-mul-1, cop):
            if(i >= 0):
                l[i] = 1
        for i in range(cop, cop+mul):
            if(i < 100):
                l[i] = 1
    print(l.count(0))
