from sys import argv
script, filename = argv

txt  = open(filename)
print("Here's your file %s" %filename)
print(txt.read())

print("Type filname again :")
file_again = input("$")

txt_again = open(file_again)

print(txt_again.read())

# use of file read and write

print("We're going to erase  %r" %filename)
print("If you don't want that , hit CTRL +c")
print("If you want that, hit Enter")

input("?")
print("open the file....")
target = open(filename,'w')
print("Turncating the file. goodbyyy!")
target.truncate()

print("Now  i'm gonig to ask you for three line. ")

line1 = input("$ line1 :")
line2 = input("$ line2 :")
line3 = input("$ line3 :")

print("Now I'm gonig to write these to the file.")

target.write(line1 )
target.write(line2 + "\n")
target.write(line3 + "\n")

print("task complete . we close it.")
target.close()