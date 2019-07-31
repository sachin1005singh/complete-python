# use of extra  function of module
import operator
li = list(input("Enter the element of list :"))

for i in range(0,len(li)):
    print(li[i], end = " ")

print("\r")

# use of setitems
operator.setitem(li,2,"sachin")
print(" After modify the list :")
for i in range(0,len(li)):
    print(li[i], end = " ")

print("\r")

# use of getitems
a= operator.getitem(li,2)
print("The use of getitems :\t",a)

# use of delitems
operator.delitem(li,2)
print("The use delitem :")
for i in range(0,len(li)):
    print(li[i], end = " ")

print("\r")


#\\\\\\\\\\
# use of setitems with slice
operator.setitem(li,slice(0,2),["sachin", "kumar"])
print(" After modify the list :")
for i in range(0,len(li)):
    print(li[i], end = " ")

print("\r")

# use of getitems with slice
ass= operator.getitem(li,slice(0,2))
print(" The use of getitems :\t",ass)

# use of delitems
operator.delitem(li,slice(0,2))
print(" The use delitem :")
for i in range(0,len(li)):
    print(li[i], end = " ")

print("\r")



#\\\\\\\\\

s1= "greeksfor"
s2 = "  greek"
print("the use of concatenate method :")
print(operator.concat(s1,s2))


if (operator.contains(s1,s2)):
    print("greekfor conatain greek.")
else:    print("greekfor doesnot conatain greek ")














