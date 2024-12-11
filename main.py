import os, platform

def ping_ip(ip):
    print(f"Pinging {ip}...")
    if platform.system() in ['Linux','Darwin']:
        response = os.system(f"ping -c 4 {ip}")
    if platform.system() == 'Windows':
        response = os.system(f"ping -n 4 {ip}")

    if response == 0: print(f"{ip} is online!")
    else: print(f"{ip} is offline.")

def main():
    ip = input("Enter the IP address to ping: ")
    ping_ip(ip)

if __name__ == "__main__":
    main()
