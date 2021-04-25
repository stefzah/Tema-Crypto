import sys
from cryptography.fernet import Fernet
import os

def Decrypt(path):


    # check if the path is a file or a folder
    if os.path.isdir(path):
        for filename in os.listdir(path):
            Decrypt(path+'/'+filename)
    else:
        # opening the key
        with open('filekey.key', 'rb') as filekey:
            for line in filekey:
                txt = line.decode()
                filename, key = txt.split(':')
                key = key.replace('\n','')
                if filename == path:
                    break
            
        # using the key
        fernet = Fernet(key)
        
        # opening the encrypted file
        with open(path, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        with open(path, 'wb') as dec_file:
            dec_file.write(decrypted)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Expected:", 2, ", Got:" , len(sys.argv))
        print("Usage: python3 decrypt.py file")
        sys.exit()

    Decrypt(sys.argv[1])
    
dir1/dir2/SecretData.ods:9CiRnXodHAbQK-01A2eTm2Vcc1c7OAlRPPA8YAsYXbE=
dir1/dir3/SecretData.ods:F13qLfMoME_8sEKY6i07UVeeoPlfzOpC1eTz9g_a9HQ=
dir1/SecretData.ods:neQcIEq7rdOVV0cKt9SMp6sYyuW-bGdgsp9bXElEWvg=
    
    
    