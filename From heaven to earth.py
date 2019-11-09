from math import sqrt
for _ in range(int(input())):
    n, v1, v2 = map(int, input().split())
    lift = 2*n/v2
    stairs = n*sqrt(2)/v1
    print('Elevator') if lift<stairs else print('Stairs')
