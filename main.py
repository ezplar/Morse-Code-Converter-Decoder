dict_morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    ' ': '/'
}


def convert_text_morse_code():
    print("Morse Code Converter!")
    input_text = input("Please input text: ").upper()
    try:
        converted_to_morse_code = [dict_morse_code[letter] for letter in input_text]
    except KeyError:
        print("Please input text composed of letters or numbers only. No spaces")
    else:
        converted_to_morse_code = [dict_morse_code[letter] for letter in input_text]
        print(f"Converted to Morse Code: {' '.join(converted_to_morse_code)}")

def decode_morse_code():
    print("Morse Code Decoder!")
    code = input("Please input code: ").split()
    key_list = list(dict_morse_code.keys())
    value_list = list(dict_morse_code.values())
    try:
        converted_to_text = [key_list[value_list.index(i)] for i in code]
    except ValueError:
        print("Please enter Morse Code only with spaces in between..")
    else:
        converted_to_text = [key_list[value_list.index(i)] for i in code]
        print(f"Decoded Morse Code: {''.join(converted_to_text).capitalize()}")


while True:
    selection = input("Please select, Convert or Decode: ").lower()
    if selection == "convert":
        convert_text_morse_code()
    elif selection == "decode":
        decode_morse_code()
    elif selection == "exit":
        break

