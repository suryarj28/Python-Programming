user = int(input("For Secret word press 1 or For Morse-code press 0: "))

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'
                   }

if user == 1:
    user_word = input("Enter the Secret word: ")
    user_word2 = user_word.upper()

    def morse_gen(word):
        final_code = ''
        for letter in word:
            if letter in MORSE_CODE_DICT:
                morse = MORSE_CODE_DICT[letter]
                final_code += morse
                final_code += ' '
        print(f"Here is your Morse code: {final_code}.")
    morse_gen(user_word2)

elif user == 0:
    user_code = input("Enter the Morse-code: ")
    code1 = user_code


    def letter_gen(code):
        list1 = []
        code_word = ''
        for letter in code:
            if letter == ' ':
                list1.append(code_word)
                code_word = ''

            else:
                code_word += letter
        # print(list1)
        final_word = ''
        for morse_code in list1:
            for keys, values in MORSE_CODE_DICT.items():
                if values == morse_code:
                    final_word += keys

        print(f"Here is Your Secret Word: {final_word}.")

    letter_gen(code1)


else:
    print("Please give inputs of 0 and 1 only")

# for morse_code in list1:
#     keys = [k for k, v in MORSE_CODE_DICT.items() if v == morse_code]
#
#     print(keys)
