# logic of dice with infinite loop
import random
while True:
    input("press enter to roll the dice")
    num = random.randint(1,6)
    print("you got ",num)
    option = input("roll again?(y/n) :")
    if option == 'n':
        break
