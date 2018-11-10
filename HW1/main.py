import time
from decrypt.decrypt import Decrypt
from encrypt.hw1 import Encrypt

if __name__=="__main__":
    flag = 1
    while flag!=0:
        print("\n\n\n")
        print("1. Caesar cipher")
        print("2. Monoalphabetic cipher")
        print("3. Playfair cipher")
        print("4. Vernam proposed the autokey system")
        print("5. Row transposition")
        print("6. Product cipher")
        print("7. Exit")
        type = input("Please choose cipher type: ")

        if type=="1":
            print("=====Caesar cipher=====")
            print("-----Encrypt-----")
            key = input("input key: ")
            text = input("input text: ")
            cipher = Encrypt.Caesar(int(key),text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_caeser(key, cipher)
            print("text after decrypt: %s"%plain_text)
        elif type=="2":
            print("=====Monoalphabetic cipher=====")
            print("-----Encrypt-----")
            key1 = input("input key first row: ")
            key2 = input("input key second row: ")
            text = input("input text: ")
            cipher = Encrypt.Monoalphabetic(key1,key2,text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_monoalphabetic(key1,key2, cipher)
            print("text after decrypt: %s"%plain_text)
        elif type=="3":
            print("=====Playfair cipher=====")
            print("-----Encrypt-----")
            key = input("input key: ")
            text = input("input text: ")
            cipher = Encrypt.Playfair(key,text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_playfair(key, cipher)
            print("text after decrypt: %s"%plain_text)
        elif type=="4":
            print("=====Vernam proposed the autokey system=====")
            key = input("input key: ")
            text = input("input text: ")
            cipher = Encrypt.Vernam(key,text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_vernam(key, cipher)
            print("text after decrypt: %s"%plain_text)
            
            
        elif type=="5":
            print("=====Row transposition=====")
            key = input("input key: ")
            text = input("input text: ")
            cipher = Encrypt.Row(key,text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_row_transposiion(key, cipher)
            print("text after decrypt: %s"%plain_text)
        elif type=="6":
            print("=====Product cipher=====")
            key_0 = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
            key = input("input key: ")
            text = input("input text: ")
            cipher = Encrypt.Product(key_0.split(),key.split(),text)
            print("Cipher text: %s"%cipher)
            print("-----Decrypt-----")
            plain_text = Decrypt.decrypt_product(key, cipher)
            print("text after decrypt: %s"%plain_text)
        elif type=="7":
            print("=====Exit=====")
            break
        else:
            print("=====please retry=====")
        time.sleep(3)