#use of operator module
import operator
a = int(input("Enter a number :"))
b= int(input("enter 2nd number :"))

print("\nthe sum is :",operator.add(a,b))
print("The substraction is :",operator.sub(a,b))
print("the Mul is :", operator.mul(a,b),"\n")

print("the Division is :",operator.truediv(a,b))
print("the floordivide is :",operator.floordiv(a,b))
print("the pow is :",operator.pow(a,b))
print("the modulas is :",operator.mod(a,b),"\n")

#use of relation operator
# use of less than
print("the  use of 'lt' check a<b or not is :",operator.lt(a,b))
print("the use of 'le' check a<= b  :",operator.le(a,b))
print("the use of 'eq'check a ==b or not :",operator.eq(a,b),"\n")

#use of greater than
print("the  use of 'gt' check a>b or not is :",operator.gt(a,b))
print("the use of 'ge' check a>= b  :",operator.ge(a,b))
print("the use of 'ne'check a !=b or not :",operator.ne(a,b))



