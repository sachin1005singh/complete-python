from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take ?")
    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man, learn to type a number.")

    if how_much <50:
        print("Nice, you;re not greedy , you win!")
        exit(0)
    else:
        dead("You greedy bastard !")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fact bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input(">")

        if next == "take honey":
            dead("The bear looks at you then slap your face off.")
        elif next =="tant bear" and not bear_moved:
            print("The bear has moved from  the door. you can go through it now.")
            bear_moved = True
        elif next =="tant bear" and  bear_moved:
            dead("The bear has moved from  the door. you can go through it now.")
            
        elif next =="open door" and  bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evi chutlhu.")
    print("He, it, whatever stares at you and you go insane. ")
    print("Do you flee for your life or eat your head?")

    next = input(">")

    if "flee" in next :
        start()
    elif "head" in next:
        dead("Well that was tasty !")
    else:
        cthulhu_room()

    def dead(why):
        print(why, "Good job!")
        exit(0)

    def start():
        print("you are in a dark room.")
        print("There is a door room.")
        print("Which one do you take ?")
        next = input(">")

        if next == "left":
            bear_room()
        elif next == "right":
            cthulhu_room()
        else:
            dead("you stumble around the room util you starve.")


    start()     
            
                  
    
        
