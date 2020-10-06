import time
import os
import pypresence
import handler
import sys

from pypresence import Presence
from os import system
from colorama import Fore, init

if os == "Windows":
	system('cls')
else:
	system('clear')
	print(chr(27) + "[2J")

time.sleep(2)

print(Fore.CYAN + """\
♥ DISCORD CUSTOM RPC ♥
""" + Fore.RESET)

print(Fore.RED + "Status: Not Running" + Fore.RESET)

client_id = input("\nClient ID (Important)\n> ")
time.sleep(3)
details = input("\nDetails (Top)\n> ")
time.sleep(3)
state = input("\nState (Bottom)\n> ")
time.sleep(3)
small_icon = input("\nSmall Icon (Type None if you don't want)\n> ")
time.sleep(3)
large_icon = input("\nLarge Icon (Type None if you don't want)\n> ")
time.sleep(3)
small_text = input("\nSmall Text\n> ")
time.sleep(3)
start = input("\nStart? [Y/N]\n> ")
#762199966973165569
if start in ['Y', 'y', 'yes', 'Yes', 'YES']:
	if os == "Windows":
		system('cls')
	else:
		system('clear')
		print(chr(27) + "[2J")

	time.sleep(2)

	print(Fore.CYAN + """\
	♥ DISCORD CUSTOM RPC ♥
	""" + Fore.RESET)

	print(Fore.GREEN + "Status: Running\n" + Fore.RESET)
	rich_presence = Presence(client_id)

	def connect():
		global rich_presence
		return rich_presence.connect()

	def connect_loop(retries=0):
		global rich_presence
		if retries > 10:
			return
		try:
			connect()
		except Exception as e:
			print(e)
			time.sleep(10)
			retries += 1
			connect_loop(retries)
		else:
			update_loop()

	print(Fore.GREEN + "[!] - Started RPC" + Fore.RESET)
	print("RPC Setup:")
	print(f"Details                  : {details}")
	print(f"State                    : {state}")
	print(f"Small Image (small icon) : {small_icon}")
	print(f"Large Image (large icon) : {large_icon}")
	print(f"Small Text               : {small_text}\n")
	print("\nLogs:")

	def update_loop(logs=1):
		global rich_presence
		start_time = int(time.time())
		try:
			while True:
				rich_presence.update(state=state,
					small_image=small_icon,
					large_image=large_icon,
					large_text='Raphiel#4045 Custom RPC',
					small_text=small_text,
					details=details,
					start=start_time
					)

				time.sleep(15)
				print(Fore.GREEN + "[Logs] - Successfully updated. ({})".format(logs) + Fore.RESET)
				logs += 1
		except Exception as e:
			rich_presence.clear()
			print(Fore.RED + e + Fore.RESET)
			time.sleep(15)
			update_loop()

	try:
		connect_loop()
	except KeyboardInterrupt:
		print(Fore.RED + "[!] - Stopped RPC" + Fore.RESET)
else:
	print("Quitting in 10 seconds")
	time.sleep(10)
	quit()