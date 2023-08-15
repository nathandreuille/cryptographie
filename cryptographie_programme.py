
from cryptography.fernet import Fernet
from tkinter import *

def fct_encrypt() : 
    user_folder = entry.get()
    folder_key = key.get()
    cipher_suite = Fernet(folder_key)
    folder = open(user_folder,"r")
    line = True
    folder_crypted = open("folder_crypted.txt","w")
    while line :    
        line = folder.readline()
        if line :
            line_byte = line.encode()
            ciphertext = cipher_suite.encrypt(line_byte)
            folder_crypted.write(f"{str(ciphertext)}\n")
    folder.close()
    folder_crypted.close()


def fct_decrypt():
    user_folder_crypted = entry.get()
    folder_key = key.get()
    cipher_suite = Fernet(folder_key)
    folder_decrypted = open("folder_decrypted.txt","w")
    line = True
    folder_crypted = open(user_folder_crypted,"r")
    while line :    
            line = folder_crypted.readline()
            line = line[1:]
            if line :
                decrypt =cipher_suite.decrypt(line)
                folder_decrypted.write(str(decrypt.decode()))
    folder_crypted.close()
    folder_decrypted.close()

user_choice = input("Taper 1 si vous voulez cripter un document, taper 2 si vous voulez decripter un document : ")
if user_choice == "1":   
    choice = "crypter"
    validation = fct_encrypt
else : 
    choice = "decrypter"
    validation = fct_decrypt
fen = Tk()
fen.geometry("500x400")
fen.configure(bg="#FF5733")
label_folder = Label(fen,text=f"Entrer le nom du fichier que vous voulez {choice} :",font = "arial 16 bold ").place(x = 70,y = 50)
label_folder = Label(fen,text="Entrer la clé de chiffrement :",font = "arial 16 bold ").place(x = 140,y = 180)
entry = Entry(fen,width=20,bg ="white",fg = "black",font = "arial 16 bold ")
entry.place(x= 160,y = 90)
key = Entry(fen,width=20,bg ="white",fg = "black",font = "arial 16 bold ")
key.place(x=160,y=220)
button_validation = Button(fen,text="valider",font = "arial 16 bold",command= validation)
button_validation.place(x=210,y=350)
fen.mainloop()










