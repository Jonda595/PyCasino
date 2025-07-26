import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def addmoney(amount: int):
    with open("m.txt", 'r+') as f:
        try:
            moneyfromfile = int(f.read())
        except:
            moneyfromfile = 0
        f.seek(0)
        f.write(str(amount + moneyfromfile))

try:
    with open("m.txt", 'x') as f:
        pass
except FileExistsError:
    pass

rars = {
    "common": 60,
    "uncommon": 50,
    "rare": 40,
    "super rare": 30,
    "epic": 15,
    "legendary": 10
}

moneyfor = {
    "common": 10,
    "uncommon": 20,
    "rare": 30,
    "super rare": 40,
    "epic": 50,
    "legendary": 100
}

clear()
print("Welcome to PyCasino!")
time.sleep(0.7)

while __name__ == '__main__':
    try:
        with open("m.txt", 'r') as f:
            money = int(f.read())
    except:
        money = 0

    print("Press ENTER to start!")
    input()

    for i in range(50):
        clear()

        r = random.choices(list(rars.keys()), weights=list(rars.values()))[0]
        print(r)

        time.sleep(0.1)

    time.sleep(0.7)

    addmoney(moneyfor[r])

    for i in range(3):
        clear()
        time.sleep(0.2)

        print(f"You got {r} for {moneyfor[r]} money!")
        time.sleep(0.3)
    
    time.sleep(1)
