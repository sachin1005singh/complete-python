#! python3
# shebang line
a =input("Enter a number \n")
y = len(a)
result =0
i = 0
while(i< y):
    
    result = result + int(a[i])
    i += 1
print(result)
