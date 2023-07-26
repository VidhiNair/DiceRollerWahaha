import random
diceroll = "Y"
nom = random.randint(1,6)
print("Welcome to the dice rolling app!")
print("Are you excited?")
yes = input("Well are you?")
print("I can't hear you!")
yese = input("Are you excited?")
print("I bet you are!")

while diceroll == "Y":
    diceroll = input("Do you want to roll? Y or N: ").upper()
    if nom == 1:
        print("[---]")
        print("[-0-]")
        print("[---]")
    elif nom == 2:
        print("[0--]")
        print("[---]")
        print("[--0]")
    elif nom == 3:
        print("[0--]")
        print("[-0-]")
        print("[--0]")
    elif nom == 4:
        print("[0-0]")
        print("[---]")
        print("[0-0]")
    elif nom == 5:
        print("[0-0]")
        print("[-0-]")
        print("[0-0]")
    elif nom == 6:
        print("[0-0]")
        print("[0-0]")
        print("[0-0]")

print("You want to leave?")
print("Why?!")
print("Don't go!")
print("You will never go!")
print("Whahahaha!")
