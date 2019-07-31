num = int(input("enter a number :"))
sum = 0
order = len(str(num))# it is important see clearfully
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //=10
    if num == sum:
        print(num,"is an armstrong number")
    else:
    	
         print(num,"is not an armstrong number")
