# program t ocopoy one file to another
from sys import argv 
from os.path import exists 

script , from_file , to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

in_file  = open(from_file).read()
#indata = in_file.read()

print("The input file is %d bytes long " %len(in_file))
print("Ready , hit enter to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w").write(in_file)
#out_file.write(in_file)

print("Alright, all done")
#out_file.close()
#in_file.close()
 