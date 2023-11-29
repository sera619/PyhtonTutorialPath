import sys, os
from charclasses import Warrior, Mage
from colorama import init, Fore

char1 = Warrior("Haudruff", 100, 10, 50)
char2 = Mage("CastALot", 60, 120, 70)
charlist = [char1, char2]
game_started = False

def start_game():
    global char1
    global char2
    global game_started
    if game_started:
        print(Fore.RED+ "[X] Game already started!" + Fore.RESET)
        main()    
    else:
        print(Fore.GREEN+"[!] Starting game...")
        print(Fore.GREEN+"[!] Initialize characters..")
        char1 = Warrior("Haudruff", 100, 10, 50)
        char2 = Mage("CastALot", 60, 120, 70)
        toggleStart()
        print(Fore.GREEN+"[!] Game successfully started!" + Fore.RESET)
        main()
    
def toggleStart():
    global game_started
    game_started = not game_started

def get_character_infos():
    print(Fore.CYAN+"[!] Current Characters:\n"+ Fore.RESET)
    color = None
    for char in charlist:
        if type(char) == Warrior:
            color = Fore.MAGENTA
        else:
            color = Fore.BLUE
        print(color+"##############################")
        char.display_info()
        print(color+"##############################\n"+Fore.RESET)
    return main()

def main():    
    options = [
        "1) Start",
        "2) Show Characters",
        "3) Damage Warrior",
        "4) Damage Mage",
        "0) Exit\n",
    ]
    print(Fore.CYAN+"\tMenu:\n")
    for o in options:
        print("\t"+o)
    option = int(input(Fore.GREEN+"[?] Enter a command: " + Fore.RESET))
    if option == 1:
        start_game()
    elif option == 0:
        raise KeyboardInterrupt
    elif option == 2:
        if not game_started:
            print(Fore.RED+"[X] You need to start the game before!" + Fore.RESET)
            return main()
        else:
            get_character_infos()
    elif option == 3:
        if not game_started:
            print(Fore.RED+"[X] You need to start the game before!" + Fore.RESET)
            return main()
        else:
            char2.attack(char1)
            char1.take_damage(char2.spell_power)
            main()
    elif option == 4:
        if not game_started:
            print(Fore.RED+"[X] You need to start the game before!" + Fore.RESET)
            return main()
        else:
            char1.attack(char2)
            char2.take_damage(char1.attack_power)
            main()
    else:
        print(Fore.RED+"[X] Invalid Command"+Fore.RESET)
        print(Fore.YELLOW +"[!] Exit game, bye!"+ Fore.RESET)
        sys.exit()
        
if __name__ == '__main__':
    init()
    try:
        os.system('cls')
        print(Fore.RED+"\t\tPython Fantasy Game\n")

        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW +"\n[!] Exit game, bye!\n"+ Fore.RESET)
    except Exception as e:
        print(Fore.RED+"[X] An error occured: "+Fore.RESET, e)
    finally:
        sys.exit()