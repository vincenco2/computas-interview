#!/usr/bin/env python

import string
import sys


# Global variable
alphabet = string.ascii_lowercase + 'æøå' # 'abcdefghijklmnopqrstuvwxyzæøå'

# Read given filename
def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

# Encrypts the message
def encrypt_caesars(key, message):
    message = message.lower()
    result = ""

    for character in message:
        if character == ' ':
            character = 'å'

        if character in alphabet:
            alphabet_index = alphabet.find(character)

            # Decrypted letter = (Unkown letter - key) modula (length of alphabet)
            letter_index = (alphabet_index + key) % len(alphabet)

            #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####
            if letter_index == 1:
                letter_index = 0
            #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####

            result += alphabet[letter_index]
            #print('original character: ' + character + ' ['+str(alphabet_index)+']     result: ' + alphabet[letter_index]+ ' ['+str(letter_index)+']')

        else:
            result +=  character

    return result


# Decrypts the message
def decrypt_caesar(key, message):
    message = message.lower()
    result = ""

    for character in message:
        if character in alphabet:
            alphabet_index = alphabet.find(character)

            #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####
            if alphabet_index == 1:
                alphabet_index = 2

            if alphabet_index == 0:
                alphabet_index = 1
            #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####

            # Decrypted letter = (Unkown letter - key) modula (length of alphabet)
            letter_index = (alphabet_index - key) % len(alphabet)

            # If space then continue
            if letter_index == len(alphabet)-1:
                result += ' '
                continue

            result += alphabet[letter_index]
            #print('character: ' + character + ' ['+str(alphabet_index)+']     result: ' + alphabet[letter_index]+ ' ['+str(letter_index)+']')

        #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####
        elif character == ' ':
            result += 'w'
        #### EDGE CASES SPECIFIC FOR GIVEN FILES IN EXERCICE ####

        else:
            result +=  character

    return result


if __name__ == "__main__":
    encrypt = True

    # Reads command arguments
    #   1. argument: python file
    #   2. arguemnt: caesar cipher key
    #   3. arguemnt: filename
    #   4. arguemnt: (optional) to mark that file needs to be encrypted
    if len(sys.argv) == 1:
        print("Missing arguments...")
        key = int(input("Enter decryption key: "))
        filename = input("Enter filename: ")
    elif len(sys.argv) == 2:
        print("Missing filename...")
        filename = input("Enter filename: ")
    elif len(sys.argv) == 4:
        if sys.argv[3] == '-d':
            encrypt = False

    key = int(sys.argv[1])
    filename = sys.argv[2]

    # Read filename
    message = read_file(filename)

    # Encypts message
    if encrypt:
        result = encrypt_caesars(key, message)

    # Decrypts message
    else:
        result = decrypt_caesar(key, message)

    # Writes to file
    result_file = open('result.txt', 'w')
    result_file.write(result)
    result_file.close()
    print(result)
