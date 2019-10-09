n = int(input())
while(n != 0):
    numbers = list(map(int, input().split()))
    numbers2 = numbers[:]
    

    for i in range(len(numbers)):
        numbers2[numbers[i] - 1] = i + 1


    if (numbers == numbers2):
        print("ambiguous")
    else:
        print("not ambiguous")

    n = int(input())
