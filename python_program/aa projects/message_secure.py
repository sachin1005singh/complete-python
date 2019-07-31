alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmsg = ''

message = input('Please enter a message :')

for character in message:
    position = alphabet.find(character)
    newpos = (position +3)
    newchar = alphabet[newpos]

    newmsg += newchar

print('your new message is', newmsg)
