import cmath
a = int(input("enter a :"))
b= int(input("enter b :"))
c = int(input("enter c :"))
d= (b**2)- (4*a*c)
ans1 = (-b + cmath.sqrt(d))/(2*a)
ans2= (-b + cmath.sqrt(d))/(2*a)
print("the solution(zeros) are {0} and {1}".format(ans1,ans2))
