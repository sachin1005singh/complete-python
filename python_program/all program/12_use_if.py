peo = int(input("Enter the numbers of people : "))
cats = int(input("Enter the numbers of cats : "))
dogs = int(input("Enter the numbers of dogs : "))

if peo < cats :
    print("To many cats! The world is doomed !")
if peo > cats:
    print("Not many cats ! The world is saved !")
	
if peo < dogs :
    print("To many dogs! The world is doomed !")
if peo > dogs:
    print("Not many dogs ! The world is saved !")
	
dogs += 5
if peo <= dogs :
    print("people are less than or equal to dogs")
if peo >= dogs:
    print("people are greater than or equal to dogs")

if peo == dogs:
    print("People are dogs")	
