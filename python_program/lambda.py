#program to use anonymous (lamda function)
milist = [1,2,3,4,5,6,7,8,9,10,11,12,13]

new_list = list(filter(lambda x:(x%2 == 0),milist))
print(new_list)
