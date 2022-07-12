import random


plainText = open('text2.txt', 'r')

ogdict = [

    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H',

    'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',

    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W',

    'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8',

    '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',

    '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', ',', '.', '>', '?',

    '\n', '\t', '\'', '\r', '\v', '\f', '–', '’', 'ł', 'í', '¿', 'é'

]



def encrypt2(plainText):

    encryption = " "

    f = open('encryption2.txt', 'w')

    for line in plainText:

        for a in line:

            cindex = ogdict.index(a)

            if cindex is not False:

                cindex = ogdict.index(a)

                encryption = encryption + newdict[cindex]

                #ogdict index value = newdict position

                #write newdict[#]

            elif cindex is not True:

                a = str(a)

                ogdict.extend(a)

                cindex = ogdict.index(a)

                encryption = encryption + ogdict[cindex]  #if not in ogdict

        w = f.write(encryption)

    #print(y,'little monkeys jumping off the bed')

    f.close



plainText.close

ogdict = [

    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H',

    'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',

    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W',

    'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8',

    '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',

    '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', ',', '.', '>', '?',

    '\n', '\t', '\'', '\r', '\v', '\f', '–', '’', 'ł', 'í', '¿', 'é'

]


x = len(ogdict)

y = random.randrange(0, x)

newdict = ogdict[y:] + ogdict[:y]

#print(newdict)

newdict2 = newdict[-y:] + newdict[:-y]

#print(newdict2)

#print (x)

#print(y)

z = str(y)

zin = 0

#decryption measure

encrypt2(plainText)


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


Written using the “repl.it” Python 3 IDE.
