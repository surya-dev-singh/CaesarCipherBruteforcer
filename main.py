import enchant
from termcolor import colored
import sys

def is_english_statement(statement):
    dictionary = enchant.Dict("en_US")
    words = statement.split()
    for word in words:
        if not dictionary.check(word):
            return False
    return True

def caesar_brute_force(ciphertext):
    result = []
    for i in range(26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shift = (ord(char) - ord('A') + i) % 26
                plaintext += chr(shift + ord('A'))
            else:
                plaintext += char
        result.append(plaintext)
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <CipherText>")
    else:
        ciphertext=sys.argv[1]
        print(f"{colored('[>>] ChiperText','cyan')} {colored(ciphertext,'yellow')}")  #"WUB KDFN PH"
        print()
        results=caesar_brute_force(ciphertext)
        for i in results:
            if is_english_statement(i):
                print(colored(i,"green"))
            else:
                print(i)            


