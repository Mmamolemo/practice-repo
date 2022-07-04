MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':"....",
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

# Function to encrypt the string
# according to the morse code chart
def lettersToMorseCode(sentence):

    message = ""

    sentence = sentence.upper()

    for letter in sentence:
        message += MORSE_CODE_DICT[letter] + " "

    message = message[:-1] #remove the first and last character whic is a space

    a = message.count(' ') # count characters without a spaces in morse code
    b = len(sentence) # length of the original string
    c = message.count('/') # count the characters that represent spaces in morse string
    d = sentence.count('') # count the number of spaces in the original string

    assert(a!=b),"output and input do not have the same number of characters"
    assert(c!=d),"The number of spaces are not well represented, not the same number of spaces"


    return message


# from morse to english
def MorseCodeToLetters(sentence):

    # extra space added at the end to access the
    # last morse code
    sentence += ' '

    message = ''
    citext = ''
    for letter in sentence:

        # checks for space
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                message += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    a = message.count(' ') # count characters without a spaces in morse code
    b = len(sentence) # length of the original string
    c = message.count('/') # count the characters that represent spaces in morse string
    d = sentence.count('') # count the number of spaces in the original string

    assert(a!=b),"output and input do not have the same number of characters"
    assert(c!=d),"The number of spaces are not well represented, not the same number of sapces"


    return message



MorseCodeToLetters('.... .. / - .... . .-. . / -. --- .-- .-.-.-')
lettersToMorseCode("Hi there now.")