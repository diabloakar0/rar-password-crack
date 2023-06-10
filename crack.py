import rarfile
import string
import itertools
import os
from colorama import Fore

doblogibidoblo = '''
coded by. diablo
Instagram: diabloakar82
Twitter: diabloakar
Discord: diablo akar#1338
'''

os.system("cls")
print(Fore.GREEN + doblogibidoblo)
rar_file = r"C:\Users\rootd\OneDrive\Masaüstü\gel\readme.rar"
found = False

def crack_rar(password):
    global found
    rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"  # unrar aracının doğru yolunu burada belirtin
    try:
        with rarfile.RarFile(rar_file) as rf:
            rf.extractall(pwd=password.encode())
            print("Şifre çözüldü:", password)
            found = True
            with open("şifre.txt", "w") as f:
                f.write(password)
                print("Şifre şifre.txt dosyasına kaydedildi.")
    except rarfile.BadRarFile:
        pass

def character_crack():
    global found
    password_length = 1
    characters = string.digits + string.ascii_letters  # Sadece rakamlar ve harfler
    while not found:
        for password in itertools.product(characters, repeat=password_length):
            password = "".join(password)
            crack_rar(password)
            if found:
                break
        password_length += 1

character_crack()
