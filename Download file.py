for case in range(int(input())):
    N, K = map(int, input().split())
    price = 0
    for i in range(N):
        time, cost = map(int, input().split())
        if K == 0:
            price += time*cost
        elif K > time:
            K -= time
        else:
            price += (time-K)*cost
            K = 0
    print(price)
