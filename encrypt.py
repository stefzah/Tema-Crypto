import sys
import os
from cryptography.fernet import Fernet

def Encrypt(path):

    # check if the path is a file or a folder
    if os.path.isdir(path):
        for filename in os.listdir(path):
            Encrypt(path+'/'+filename)
    else:
        # key generation
        key = Fernet.generate_key()

        # string the key in a file
        with open('filekey.key', 'ab') as filekey:
            filekey.write(str.encode(path+":"))
            filekey.write(key)
            filekey.write(str.encode('\n'))

        # using the generated key
        fernet = Fernet(key)
        
        # opening the original file to encrypt
        with open(path, 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and 
        # writing the encrypted data
        with open(path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Expected:", 2, ", Got:" , len(sys.argv))
        print("Usage: python3 encrypt.py file")
        sys.exit()

    Encrypt(sys.argv[1])


    
    
    