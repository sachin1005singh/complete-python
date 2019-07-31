# -*- coding: utf-8 -*-
#more variable
print ("Marry had a little lamb")
print("Its fleece was white as  %rs." %'snow')
print("And everywhere that Mary went .")
print("."*10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5  = "s"
end6  = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print ( end1 + end2 + end3 + end4 + end4 + end5 + end6 ,\
end7 + end8 + end9 + end10 + end11 +end12)
print( end7 + end8 + end9 + end10 + end11 +end12)

print("-"*20)
# use of formatter like %s,%d
formatter = " %r %r %r %r "

print(formatter %(1,2,3,4))
print(formatter %("one", "two " , "three" , "four" ))
print(formatter %(True , False,False, True ))
print(formatter %(formatter,formatter , formatter, formatter))
print(formatter %("my name is sachin ",
"i love to play music" , 
'but i like to dace also ',
"thats all."))




