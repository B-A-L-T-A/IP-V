import time
RED = '\033[31m'
WHITE = '\033[37m'

while True:
    def ip_checker(ip_address):
        try:
            separated_address = ip_address.split('.')
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


    print(RED + """
     ____  ____      _  _ 
    (_  _)(  _ \ ___( \/ ) ->Balta
     _)(_  )___/(___)\  / 
    (____)(__)        \/  
    """)
    user_in = input(WHITE + "-> Ingrese la dirección IP: ")
    if ip_checker(user_in):
        print(f"Genial!!! {user_in} es una dirección IP válida! ")
    else:
        print(f"Uuupppsss!!! {user_in} NO es una dirección IP válida! ")

    time.sleep(3)
