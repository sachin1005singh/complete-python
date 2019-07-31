#program to check it is keyword or not
import keyword
s= "sachin"
s1 = "True"
s2 ="kumar"
s3 = "yield"

if keyword.iskeyword(s):
    print("this is keyword : {}".format(s))

else:
    print("not a key word")
    

if keyword.iskeyword(s1):
    print("this is keyword : {}".format(s1))

else:
    print("not a key word")
    
if keyword.iskeyword(s2):
    print("this is keyword : {}".format(s2))

else:
    print("not a key word")



if keyword.iskeyword(s3):
    print("this is keyword : {}".format(s3))

else:
    print("not a key word")


#//////////////////////
# to print all keyword

print("All keyword in python are :")
print(keyword.kwlist)


    
    








