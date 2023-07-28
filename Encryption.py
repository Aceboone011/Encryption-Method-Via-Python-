import random

#open and read file named 'SampleText.txt'
#establish a list of strings containing ALL characters
#ogdict == Original Dictionary


plainText = open('SampleText.txt', 'r')
ogdict = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H',
    'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W',
    'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
    '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
    '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', ',', '.', '>', '?',
    '\n', '\t', '\'', '\r', '\v', '\f', '–', '’', 'ł', 'í', '¿', 'é']

# define encryption function
def encrypt2(plainText):
#empty string
    encryption = ""
    f = open('encryption2.txt', 'w')

#create and write in new file
    for line in plainText:
        for a in line:
            cindex = ogdict.index(a)
            if cindex is not False:
#The character at the corresponding index is now written in the encryption string
#write newdict[#]
                encryption = encryption + newdict[cindex]
# If a character is not in the original dictionary(ogdict)then, the character is converted to a string representation, regardless of its original data type.
            elif cindex is not True:
                a = str(a)
                ogdict.extend(a)
#add the new character to the original dictionary                
                cindex = ogdict.index(a)
                encryption = encryption + ogdict[cindex]
#if not in ogdict
        w = f.write(encryption)
    f.close
plainText.close



#Method to choose a number at random: get the amount of character in ogdict and choose a number at random
x = len(ogdict)
y = random.randrange(0, x)
#shift index and reassign new dictionary to new variable: newdict
newdict = ogdict[y:] + ogdict[:y]
newdict2 = newdict[-y:] + newdict[:-y]
z = str(y)
#convert random number chose to string data type


#decryption measure
encrypt2(plainText)

#read the string in z and conver that to a predetermined code that is produced alongside the encrypted messege

for line in z:
    for num in line:
        f2 = open('encryption2.txt', 'a')
        axe = []
        if num == '1':
            axe += 'AA'

        elif num == '2':
            axe += 'AB'

        elif num == '3':
            axe += 'AT'

        elif num == '4':
            axe += 'AC'

        elif num == '5':
            axe += 'AD'

        elif num == '6':
            axe += 'AE'

        elif num == '7':
            axe += 'AG'

        elif num == '8':
            axe += 'AF'
            
        elif num == '9':
            axe += 'AU'
            
        else:
            axe += 'AP'

    h = '\n'
    f2.write(h)
    g = '\n'.join(map(str, axe))
    f2.write(g)
    f2.close()
