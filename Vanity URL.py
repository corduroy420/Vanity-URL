import clipboard
import time
from colorama import Fore, init
import os
init(convert=True)



intro = f"""{Fore.RED}

		__   __         _ _          _   _ ___ _      _                         _                   
		\ \ / /_ _ _ _ (_) |_ _  _  | | | | _ \ |    | |__ _  _   __ ___ _ _ __| |_  _ _ _ ___ _  _ 
		 \ V / _` | ' \| |  _| || | | |_| |   / |__  | '_ \ || | / _/ _ \ '_/ _` | || | '_/ _ \ || |
		  \_/\__,_|_||_|_|\__|\_, |  \___/|_|_\____| |_.__/\_, | \__\___/_| \__,_|\_,_|_| \___/\_, |
		                      |__/                         |__/                                |__/ 
{Fore.RESET}
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 1:{Fore.RESET} Start
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 2:{Fore.RESET} Discord 
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 3:{Fore.RESET} Restart


"""
cls = lambda: os.system('cls')

def discord(link):
    os.system('start ' + link)

def vanityurl():
	print(f'[{Fore.RED}>{Fore.RESET}] Server Invite Code', end=''); server = str(input('  :  '))
	if server == "exit" or server == "3" or server == "restart":
		cls()
		start()
	else:
		pass
	print(f'[{Fore.RED}>{Fore.RESET}] Vanity Text', end=''); invite = str(input('  :  '))
	text = "discοrd.gg/" + invite + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + server
	clipboard.copy(text)
	print(f'[{Fore.RED}>{Fore.RESET}] {Fore.LIGHTGREEN_EX}Copyed to clipboard!')
	input()


def start():
	print(intro)
	print(f'[{Fore.RED}>{Fore.WHITE}] Your choice', end=''); choice = str(input('  :  '))
	if choice == '1':
		vanityurl()
	elif choice == "2":
		discord("https://discord.gg/VRccYxe")
		cls()
		start()
	elif choice == "3":
		cls()
		start()
	else:
		print()
		print(f"[{Fore.RED}>{Fore.WHITE}] {Fore.RED}INVALID INPUT OPTION")
		time.sleep(1.5)
		cls()
		print(intro)
		print(f'[{Fore.RED}>{Fore.WHITE}] Your choice', end=''); choice = str(input('  :  '))
		if choice == '1':
			vanityurl()		



if __name__ == '__main__':
	start()
       
