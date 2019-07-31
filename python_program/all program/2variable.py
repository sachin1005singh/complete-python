car = 100
space_in_car = 4.0
drivers = 30
passengers = 90
car_not_drivers = car - drivers
car_driven = drivers
carpool_capacity = car_driven *space_in_car
av_pass = passengers/car_driven

print("This are ", car , "car available.")
print("This will be ", car_not_drivers,"empty car")
print("We can transport", carpool_capacity," people today")
print("We have ", passengers, "to carpool today")
print("We need to put about", av_pass ,"in each car")


#----------------------------------------------
print("------------------------------------------------")

my_name = 'Zed a.shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = "white"
my_hair = 'Brown'

print("Let's talk about %s" %my_name)
print("He's %d inchestall" %my_height)
print("he's %d pound heavy" %my_weight)

print("Actually that not to heavy" )
print("He's got %s eyes and %s hair" %(my_eyes,my_hair))

print("------------------------------------------------")

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s types of people %s"%(binary, do_not)

print(x)
print(y)

print("I said %r." %x)
print("Ialso said: %s" %y)

hilarious = True
joke_eval = "Isn't that joke so funny ? ! %r"
print(joke_eval % hilarious)

w = "This is the left side of .."
e = "a string with a right side"
print(w + e)





