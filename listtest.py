#I made this one to test lists, I grabbed 5 fun facts from "https://www.sciencefocus.com/science/fun-facts" and put them on a list
import random
from colorama import Fore, Back, Style, init
import time
list=["Did you know? Leftover pasta has extra health benefits", "Did you know? The raw ingredients of a human body would cost over £116,000", "Did you know? Mars isnt actually round", "Did you know? The Universe's average colour is called 'Cosmic latte'", "Did you know? Parents in the US consistently rank as the world's unhappiest"]
randomvalue = random.randrange(len(list))
print(Fore.YELLOW + "Computer! Give me a fun fact")
time.sleep(2)
print(Fore.BLUE + "Uhhhh...")
time.sleep(1)
print(Fore.BLUE + list[randomvalue])
time.sleep(2)
print(Fore.YELLOW + "Wow computer! That is so cool.")
