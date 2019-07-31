"""# use of class
class parrot:
    spe = "birds"

    def __init__(self, name, age ):
        self.name = name
        self.age= age

blu = parrot("amit",10)
bluu = parrot("ajay",12)

print("blu is a {} ".format(blu.__class__.spe))
print("{} is {} year old ".format(blu.name,blu.age))
print("{} is {} year old ".format(bluu.name,bluu.age))
"""



#//////////
class parr:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,sing):
        return("{} sings {}".format(self.name,sing))

    def dance(self):
        return("{} is now dancing".format(self.name))

ob1 = parr("mill",45)
print(ob1.sing("happy"))

print(ob1.dance())
 
