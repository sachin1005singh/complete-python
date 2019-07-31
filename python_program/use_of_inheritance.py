class base:
    def base_fun(self,name):
        self.name = name
        print("your name is {}".format(self.name))
        print("hellow i am base")

class child(base):

    
    
    def sk(self):
        print("i am child class")
        return("you are in child class")

ob1 = child()
ob1.sk()
ob1.base_fun("sachin")

#multiple inhertance program


class father:
    def father(self,fname):
        self.fname = fname
        print("mrs. {} ".format(self.fname))

class mother:
    def mom(self, mname):
        self.mname = mname
        print("mrs . {}".format(self.mname))


class childs(father,mother):
    def bio(self,name,age):
        self.name = name
        self.age = age
        print("we are parents of  {}\n and his/her age is {} ".format(self.name,self.age))
        print("my parents name is MR: {} and mother name is Mrs :{}".format(self.fname,self.mname))

pass    

ob1 = childs()
ob1.father("narender")
ob1.mom("kushum")
ob1.bio("amit", 16)
