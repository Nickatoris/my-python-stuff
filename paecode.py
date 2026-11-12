#I made this one for fun when I started Python, I wanted to make something for my girlfriend, I wanted to test infinite prints and colored text aswell.
from colorama import Fore, Back, Style, init
init(autoreset=True)


cutelevel = int(input("1-100 How cute is paepae? ^^: "))
if cutelevel >= 100:
    print("Correct! :D")
else:
    while True:
        print(Fore.RED + "WRONG!")
