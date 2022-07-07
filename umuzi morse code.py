morseCodeDict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    "@": ".--.-.",
    "=": "-...-",
    "!": "-.-.--",
    '"': ".-..-.",
    ":": "---...",
    "x": "-..-",
    "+": ".-.-.",
    "_": ". . _ _ . _",
}

def lettersToMorseCode(sentence):
    morse_code_output = ""
    sentence = sentence.upper()
    if sentence == "":
        return ".-..-. .-..-."
    if len(sentence) > 0:
        for letter in sentence:
            morse_code_output += morseCodeDict[letter] + " "
        morse_code_output = morse_code_output[:-1]

    assert len(morse_code_output.split(" ")) == len(
        sentence
    ), "output and input do not have the same number of characters"
    assert morse_code_output.count("/") == sentence.count(
        " "
    ), "The number of spaces are not well represented, not the same number of spaces"

    return morse_code_output


def morseCodeToLetters(sentence):
    sentence += " "
    letters_output = ""
    text = ""

    for letter in sentence:
        word = 0
        if letter != " ":
            word = 0
            text += letter
        else:
            word += 1
            if word == 2:
                letters_output += " "
            else:
                letters_output += list(morseCodeDict.keys())[
                    list(morseCodeDict.values()).index(text)
                ]
                text = ""

    assert len(letters_output.split(" ")) == len(
        sentence.split("/")
    ), "output and input do not have the same number of characters"
    assert letters_output.count(" ") == sentence.count(
        "/"
    ), "The number of spaces are not well represented, not the same number of sapces"

    return letters_output

print(lettersToMorseCode('hi there'))
