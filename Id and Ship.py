t = int(input())

for i in range(t):
    a = input()
    if a.lower() == 'b':
        print("BattleShip")
    elif a.lower() == 'c':
        print("Cruiser")
    elif a.lower() == 'd':
        print("Destroyer")
    elif a.lower() == 'f':
        print("Frigate")    
