#!/usr/bin/env python3

import os
import subprocess
import socket
import platform
import time
import random


# ========================= UTILITIES =========================

def clear_screen():
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')


def print_banner():
    print("""
=====================================================
        NETWORK & WIFI DIAGNOSTIC TOOL
                SupremeModz Edition
=====================================================
""")


def slowprint(text, speed=0.005):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()


# ========================= IP VALIDATOR =========================

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_ip_menu():
    ip = input("\nEnter IP to validate: ")
    if is_valid_ip(ip):
        print(f"✔ VALID IP: {ip}")
    else:
        print(f"✘ INVALID IP: {ip}")


# ========================= LOCAL NETWORK INFO =========================

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unavailable"


def show_local_info():
    slowprint("\nFetching local network information...")
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    osys = f"{platform.system()} {platform.release()}"

    print(f"\n🖥 Hostname: {hostname}")
    print(f"📡 Local IP: {local_ip}")
    print(f"🧪 Platform: {osys}")


# ========================= PING TEST =========================

def ping(host, count=4):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        slowprint("\nRunning ping test...")
        result = subprocess.run(
            ["ping", param, str(count), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Error: {e}"


def ping_menu():
    host = input("\nEnter IP/Host to ping: ")
    print(ping(host))


# ========================= DNS LOOKUP =========================

def dns_lookup(domain):
    try:
        slowprint("\nResolving DNS...")
        ip = socket.gethostbyname(domain)
        return f"{domain} → {ip}"
    except Exception as e:
        return f"DNS Error: {e}"


def dns_menu():
    domain = input("\nEnter domain (e.g. google.com): ")
    print(dns_lookup(domain))


# ========================= SIMULATED SPEED TEST =========================

def simulate_speed_test():
    slowprint("\nRunning safe simulated speed test...")

    for _ in range(25):
        print("▉", end="", flush=True)
        time.sleep(0.04)

    print("\n")
    download = round(random.uniform(20, 250), 2)
    upload = round(random.uniform(5, 120), 2)
    ping_ms = round(random.uniform(5, 60), 2)
    return download, upload, ping_ms


def speed_test_menu():
    down, up, ping_ms = simulate_speed_test()
    print(f"📥 Download Speed: {down} Mbps")
    print(f"📤 Upload Speed: {up} Mbps")
    print(f"🏓 Ping: {ping_ms} ms")


# ========================= SUSPENDED SITE PLACEHOLDER =========================

def show_suspended_site_example():
    url = "http://example-suspended-site.com"
    msg = "THIS SITE HAS BEEN SUSPENDED"

    print("\n+--------------------------------------------------+")
    print(f"|  {url}")
    print(f"|  {msg}")
    print("+--------------------------------------------------+")

    save = input("Save this in suspended_links.txt? (y/n): ").lower()
    if save == "y":
        with open("suspended_links.txt", "a") as f:
            f.write(f"{time.ctime()} - {url} - {msg}\n")
        print("Saved.")


# ========================= REPORT =========================

def generate_report(include_suspended=False):
    slowprint("\nGenerating diagnostic report...\n")

    hostname = socket.gethostname()
    local_ip = get_local_ip()

    try:
        google_ip = socket.gethostbyname("google.com")
    except:
        google_ip = "Unavailable"

    report = [
        "==================== NETWORK REPORT ====================\n",
        f"Generated: {time.ctime()}\n",
        f"Hostname: {hostname}\n",
        f"OS: {platform.system()} {platform.release()}\n",
        f"Local IP: {local_ip}\n",
        f"DNS: google.com → {google_ip}\n\n",
        "Simulated Speed Test:\n",
        f"  Download: {round(random.uniform(20, 200), 2)} Mbps\n",
        f"  Upload:   {round(random.uniform(5, 120), 2)} Mbps\n",
        f"  Ping:     {round(random.uniform(5, 60), 2)} ms\n"
    ]

    if include_suspended:
        report.append("\nSuspended Sites (placeholder):\n")
        report.append(" - http://example-suspended-site.com [SUSPENDED]\n")

    final_report = "".join(report)
    print(final_report)

    with open("network_report.txt", "w") as f:
        f.write(final_report)

    print("📄 Saved as: network_report.txt")


# ========================= MENU =========================

def menu():
    print("""
==================== MENU =====================

1. Validate IP Address
2. Show Local Network Info
3. Ping Test
4. DNS Lookup
5. Run Speed Test
6. Generate Network Report
7. Show Suspended Site Example
8. Exit

==============================================
""")
    return input("Choose an option: ")


# ========================= MAIN =========================

def main():
    clear_screen()
    print_banner()
    slowprint("Initializing Network Diagnostic Tool...\n")

    while True:
        choice = menu()

        if choice == "1":
            validate_ip_menu()
        elif choice == "2":
            show_local_info()
        elif choice == "3":
            ping_menu()
        elif choice == "4":
            dns_menu()
        elif choice == "5":
            speed_test_menu()
        elif choice == "6":
            add = input("Include suspended entries? (y/n): ").lower()
            generate_report(include_suspended=(add == "y"))
        elif choice == "7":
            show_suspended_site_example()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        input("\nPress ENTER to return to menu...")
        clear_screen()


if __name__ == "__main__":
    main()