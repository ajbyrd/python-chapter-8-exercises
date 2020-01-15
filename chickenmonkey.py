
def chickenMonkey():
    for i in range(1, 101):
        if i % 5 == 0 and i % 7 == 0:
            print("ChickenMonkey")
        elif i % 5 == 0:
            print("Chicken")
        elif i % 7 == 0:
            print("Monkey")
        else:
            print(i)

print(chickenMonkey()) 