from os import path
import time
alphabets = 'abcdefghijklmnopqrstuvwxyz'
key = 5
def enter_Message():
    message = input('Message: ')
    encrypt_Message = ''
    for i in message:
        pos = alphabets.find(i)
        newpos = (pos+5)%26
        encrypt_Message += alphabets[newpos]
    msg_File = open('message.txt', 'w')
    msg_File.write(encrypt_Message)
    msg_File.close()

def decrypt_Message():
    decrypt_msg = ''
    msg_File = open('message.txt', 'r')
    msg_file_decrypt_read = msg_File.read()
    msg_File.close()
    for i in msg_file_decrypt_read:
        depos = alphabets.find(i)
        newdepos = (depos-5)%26
        decrypt_msg += alphabets[newdepos]
    password_File = open('password.txt', 'r')
    decrypt_encrypted_password = password_File.read()
    password_File.close()
    decrypt_Password = ''
    for i in decrypt_encrypted_password:
        deposition = alphabets.find(i)
        newdeposition = (deposition-5)%26
        decrypt_Password += alphabets[newdeposition]
    enter_Pwd = input('Password: ')
    if enter_Pwd == decrypt_Password:
        print(decrypt_msg)
        time.sleep(9999)
        


def take_Password():
    password = input("Password: ")

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    key = 5
    encrypt_Password = ''
    for i in password:
        position = alphabets.find(i)
        newposition = (position+5)%26
        encrypt_Password += alphabets[newposition]
    password_File = open('password.txt', 'w')
    password_File.write(encrypt_Password)
    password_File.close()
    ask_Option()

def ask_Option():
    option = input('DO you wnt to encrypt or decrypt? ')
    if option == 'encrypt':
        enter_Message()
    elif option == 'decrypt':
        decrypt_Message()

if path.exists('password.txt') == True:
    ask_Option()


else:
    take_Password()
