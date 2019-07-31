def hcfuse(x,y):
    if x>y:
        small = y
    else:
        small = x
    for i in range(1,small+1):
        if((x%i == 0)and (y%i== 0)):
            hcf = i
    return hcf

a= int(input("enter an number :"))
b= int(input("enter an number :"))

print("H.C.F of ",a," and ", b , " is ", hcfuse(a,b))
