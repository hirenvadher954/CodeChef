for _ in range(int(input())):
    X,Y,K = list(map(int,input().split()))
    if ((X+Y)//K + 1)%2 == 1:
        print('Chef')
    else:
        print('Paja')
