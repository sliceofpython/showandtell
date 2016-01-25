'''
Morse
Chra94

Practice. Difficult to decode morse sentences.
CODE segment and idea stolen from https://arnvanhoutte.be/Blog/Details/20
'''


CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

reverse_code = {'!': ' '}
for k, v in CODE.items():
    reverse_code[v] = k



def morse_to_text():
#TODO: Fix word detection.
    message = ''
    print('Seperate morse letters with space, \n'
           'seperate words with: space, !, space \n'
           'Example: .- ! .- = A A')

    morse = input('enter morse').split()
    for char in morse:
        message += reverse_code[char]

    print(message)
    while True:
        pass

def text_to_morse():
    message = input('Enter message.')
    return_message = ''
    for char in message:
        if char.isalnum():
            return_message += CODE[char.upper()] + ' '
            #CODE[char.upper()].join(return_message)
        elif char is ' ':
            return_message += '   '
    print(return_message)
    while True:
        pass


mode = input('Input morse or text?')
if mode == 'morse':
    morse_to_text()
else:
    text_to_morse()
