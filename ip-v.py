import time
from colorama import init, Fore
import os

os.system("clear")

loop = tqdm(total=30000, position=0, leave=False)
for k in range(30000):
    loop.set_description(Fore.LIGHTRED_EX + 'Opening Script'.format(k))
    loop.update(1)
loop.close()

while True:
    def ip_checker(ip_address):
        try:
            separated_address = ip_address.split('.')
            # print(separated_address)
            valid_ip = 0
            for i in separated_address:
                if int(i) >= 0 and int(i) <= 255:
                    valid_ip += 1
            if valid_ip == 4:
                return True
            else:
                return False
        except:
            return False


    print(Fore.YELLOW + """                                                                                                 
       ___         ___           ___     
      /__/\       /  /\         /  /\    
      \__\:\     /  /::\       /  /:/    
      /  /::\   /  /:/\:\     /  /:/     
   __/  /:/\/  /  /::\ \:\   /__/:/  ___ 
  /__/\/:/~~  /__/:/\:\_\:\  |  |:| /  /\ 
  \  \::/     \__\/  \:\/:/  |  |:|/  /:/
   \  \:\          \  \::/   |__|:|__/:/ 
    \__\/           \__\/     \__\::::/  
                                  ~~~~""")
    print(Fore.YELLOW + "C", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "d", end="")
    print(Fore.RED + "e", end="")
    print(Fore.CYAN + "d ", end="")
    print(Fore.MAGENTA + "b", end="")
    print(Fore.WHITE + "y ", end="")
    print(Fore.YELLOW + "B", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "l", end="")
    print(Fore.GREEN + "t", end="")
    print(Fore.BLUE + "a", end="")
    print("\n")
    user_in = input(Fore.YELLOW + ">>> Enter the IP address: ")
    if ip_checker(user_in):
        print(f"Great!!! {user_in} is a valid IP address! ")
    else:
        print(f"Uuupppsss!!! {user_in} It is NOT a valid IP address! ")

    time.sleep(3)
