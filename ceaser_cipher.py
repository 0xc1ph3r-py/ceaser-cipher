import pyperclip
import sys

print("Ceaser cipher :-")
def ceaser(message, key, mode):
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            text_index = SYMBOLS.find(symbol)
            if mode == "e":
                text_index = (text_index + key )% len(SYMBOLS)
                translated += SYMBOLS[text_index]
            elif mode == "d":
                text_index = (text_index - key )% len(SYMBOLS)
                translated += SYMBOLS[text_index]
        else:
            translated += symbol

    return translated

while True:
    mode = input("Do you wanna encrypt or decrypt (e, d or q to Quit): ").lower()
    if mode == "q":
        sys.exit()
    key = int(input("Enter a key to shift values: "))
    message = input("Enter a message to encrypt or decrypt: ").upper()
    translated = ceaser(message, key, mode)
    print(f"Translated message > {translated}")
    try:
        pyperclip.copy(translated)
        print("Text copied to clipboard...")
    except Exception as e:
        print(f"Error while copying to clipboard {e}")

    



            
