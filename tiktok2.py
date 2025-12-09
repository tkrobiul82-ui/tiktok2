from os import system as c
import time
import random
import os

G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def banner():
    c("clear")
    print(f"""{G}
╔══════════════════════════════════╗
║     RIMON  WORLD - TIKTOK VIP   ║(NON ROOT)")
╚══════════════════════════════════╝
{Y}         FOLLOWER INCREASER TOOL


    else:
        print(f"{G}[✓]TiK tok followers Injectior!\n")
        time.sleep(1)

def main():
    banner()
   
    username = input(f"{C}Enter TikTok Username: {W}@")
    print(f"\n{Y}[+] Connecting to TikTok Secure Server...")
    time.sleep(2)
    print(f"{G}[✓] User Found: @{username}")
    print(f"{C}[+] Injecting VIP Followers...\n")

    for i in range(1, 6):
        followers = random.randint(100, 2000)
        print(f"{W}[{i}] Added {followers} followers...")
        time.sleep(1)

    print(f"\n{G}[✓] SUCCESS! VIP Follower Injection Completed.")
    print(f"{C}Now your profile looks like a PRO 😎\n")
    input(f"{W}Press Enter to Exit...")