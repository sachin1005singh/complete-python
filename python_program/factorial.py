# program to find factorial of an number
def factfind(x):
    if x == 1:
        return 1
    else:
        return(x*factfind(x-1))

num = int(input("Enter an number :"))
print("The factorial of %d is :"%num,factfind(num))
    
