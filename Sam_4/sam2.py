import random

def roll_dice():
    dice = random.randint(1, 6)
    print(f"Выпало число {dice}")
    if dice == 5 or dice == 6:
        print("Вы победили")
    elif dice == 3 or dice == 4:
        roll_dice()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    roll_dice()
