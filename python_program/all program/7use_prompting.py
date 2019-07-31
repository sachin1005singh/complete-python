# use of prompting and passing
from sys import argv
script , user_name = argv

promt = "$"

print("Hi %s, I'm th %script" %(user_name,script))
print(" I'd like t oask you  few question.")
print("Do you like me %s" %user_name)

like = input(promt)

print("Where do you live %s" %user_name)
lives = input(promt)

print("What kind of computer do you have ?")
computer =input()

print("""
Alright, so you said %s about liking me, 
you live in %r. Not sure where that is .
And you have a %r computer . nice
""" %(like, lives , computer))

