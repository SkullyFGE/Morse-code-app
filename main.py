def morse_database():
    '''
    Database for morse alphabet with letters and morse equivalents.
    '''
    morse_alphabet = {
        # Letters
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        # Digits
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        # Punction Mark
        "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.", ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-", "-": "-....-", "×": "-..-",
        "+": ".-.-.", "\"": ".-..-.", "?": "..--..", "/": "-..-.", " ": " "
    }
    reversed_morse_alphabet = dict()

    for key, value in morse_alphabet.items():
        reversed_morse_alphabet[value] = key

    return morse_alphabet, reversed_morse_alphabet


def user_interaction():
    '''
    Welcoming message for the user and set-up for variables, that are used later in the code.
    '''
    print("\nHello, welcome to my morsecode app")

    while True:
        print("Do you want to encrypt (e) or decrypt (d) a message?\n")
        choice = str(input("Enter you choice: ").lower().strip())

        if choice in ["encrypt", "decrypt", "e", "d"]:
            break
        else:
            print("Enter valid input!")

    message = str(input("Enter you message: ").lower().strip())

    return choice, message


def code_message(user_choice, user_message, morse_dict, reverse_morse_dict):
    '''
    Process that encrypts a message.
    '''
    result = ""

    if user_choice == "encrypt" or user_choice == "e":
        for letter in user_message:
            if letter in morse_dict:
                result += morse_dict[letter] + "/"
            else:
                result += "?"
        return result

    elif user_choice == "decrypt" or user_choice == "d":
        morse_message = user_message.split("/")
        for symbol in morse_message:
            if symbol in reverse_morse_dict:
                result += reverse_morse_dict[symbol] + ""
            elif symbol == "":
                continue
            else:
                result += "?"  # Unknown letters/symbols
        return result

    else:
        print("Enter a valid operation!")

'''
Process that runs the program:
'''        

set_morse, set_reversed_morse = morse_database()

user_choice, user_message = user_interaction()

final_output = code_message(
    user_choice, user_message, set_morse, set_reversed_morse)

print(f"\nResult is: {final_output}\n")
