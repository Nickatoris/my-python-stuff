from colorama import Fore, Back, Style, init
init(autoreset=True)


cutelevel = int(input("1-100 How cute is paepae? ^^: "))
if cutelevel >= 100:
    print("Correct! :D")
else:
    while True:
        print(Fore.RED + "WRONG!")