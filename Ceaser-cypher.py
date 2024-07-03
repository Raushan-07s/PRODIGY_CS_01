'''
Task-01
Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.

'''

def encrypt(text,s):

    result = ""
 

    # traverse text

    for i in range(len(text)):

        char = text[i]
 

        # Encrypt uppercase characters

        if (char.isupper()):

            result += chr((ord(char) + s-65) % 26 + 65)
 

        # Encrypt lowercase characters

        else:

            result += chr((ord(char) + s - 97) % 26 + 97)
 

    return result
