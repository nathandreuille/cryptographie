from cryptography.fernet import Fernet 
with open("folder_key","w") as folder :
    for i in range(10):
        key = Fernet.generate_key()
        folder.write(f"{str(key)}\n")
