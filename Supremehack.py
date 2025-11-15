#!/usr/bin/env python3

"""
SUPREME NETWORK & NUMBER TOOL
Author: SupremeModz (Updated Version)

Features:
- IP Validator
- Local Network Info
- Ping Test
- DNS Lookup
- Simulated Speed Test
- Number Checker / Telco Detector
- Suspended Site Placeholder
- Network Report Generator
- Pure built-in Python modules
"""

import os
import subprocess
import socket
import platform
import ipaddress
import time
import random

# --------------------------- UTILITIES ---------------------------

def clear_screen():
    try:
        os.system('cls' if platform.system().lower() == 'windows' else 'clear')
    except:
        pass


def print_banner():
    banner = r"""
======================================================
     SUPREME NETWORK & NUMBER DIAGNOSTIC TOOL
======================================================
"""
    print(banner)


def slowprint(text, speed=0.003):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(speed)
    print()


# --------------------------- IP VALIDATOR ---------------------------

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False


def validate_ip_menu():
    ip = input("\nEnter IP to validate: ")
    if is_valid_ip(ip):
        print(f" ✔ VALID IP: {ip}")
    else:
        print(f" ✘ INVALID IP: {ip}")


# --------------------------- LOCAL NETWORK INFO ---------------------------

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
    platform_info = f"{platform.system()} {platform.release()}"

    print(f"\n 🖥 Hostname: {hostname}")
    print(f" 📡 Local IP: {local_ip}")
    print(f" 🧪 Platform: {platform_info}")


# --------------------------- PING TEST ---------------------------

def ping(host, count=4):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), host]

    try:
        slowprint("\nRunning ping test...")
        output = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return output.stdout if output.stdout else output.stderr
    except Exception as e:
        return f"Error: {e}"


def ping_menu():
    host = input("\nEnter IP/Host to ping: ")
    print(ping(host))


# --------------------------- DNS LOOKUP ---------------------------

def dns_lookup(domain):
    try:
        slowprint("\nResolving DNS...")
        ip = socket.gethostbyname(domain)
        return f"{domain} → {ip}"
    except Exception as e:
        return f"DNS Error: {e}"


def dns_menu():
    domain = input("\nEnter domain (example: google.com): ")
    print(dns_lookup(domain))


# --------------------------- SIMULATED SPEED TEST ---------------------------

def simulate_speed_test():
    slowprint("\nRunning safe simulated speed test...")

    for i in range(20):
        print("▉", end="", flush=True)
        time.sleep(0.05)
    print("\n")

    download = round(random.uniform(20, 250), 2)
    upload = round(random.uniform(5, 120), 2)
    ping_ms = round(random.uniform(5, 60), 2)

    return download, upload, ping_ms


def speed_test_menu():
    down, up, latency = simulate_speed_test()
    print(f" 📥 Download Speed: {down} Mbps")
    print(f" 📤 Upload Speed: {up} Mbps")
    print(f" 🏓 Ping: {latency} ms")


# --------------------------- NUMBER CHECKER / TELCO DETECTOR ---------------------------

def number_checker():
    num = input("\nEnter mobile number (PH): ").strip()

    if not num.isdigit() or len(num) not in [10, 11]:
        print("\n ✘ Invalid number format.")
        return

    # Convert to correct PH prefix
    if len(num) == 11 and num.startswith("09"):
        prefix = num[2:5]
    elif len(num) == 10 and num.startswith("9"):
        prefix = num[1:4]
    else:
        print("\n ✘ Cannot detect telco.")
        return

    # Telco prefix database
    telco_data = {
        "GLOBE / TM": [
            "905","906","915","916","917","926","927","935","936",
            "937","945","955","956","965","966","967"
        ],
        "SMART / TNT / SUN": [
            "908","909","910","912","918","919","920","921","928",
            "929","930","938","939","940","946","947","948","949"
        ],
        "DITO": [
            "895","896","897","898","899"
        ]
    }

    # Telco detection
    telco = "UNKNOWN / NEW PREFIX"
    for provider, prefixes in telco_data.items():
        if prefix in prefixes:
            telco = provider
            break

    # Sim estimation
    if telco == "GLOBE / TM":
        sim_type = "Prepaid (Estimated)"
    elif telco == "SMART / TNT / SUN":
        sim_type = "Prepaid/Postpaid (Estimated)"
    elif telco == "DITO":
        sim_type = "VoLTE Required"
    else:
        sim_type = "Unknown"

    # Display
    print("\n================ PHONE NUMBER CHECKER ================\n")
    print(f"Phone Number: {num}")
    print(f"Carrier: {telco}")
    print(f"Type: {sim_type}")
    print(f"Status: Format valid")
    print(f"Region: Philippines")
    print("\n======================================================")


# --------------------------- SUSPENDED SITE PLACEHOLDER ---------------------------

def show_suspended_site_example():
    suspended_url = "http://example-suspended-site.com"
    notice = "THIS SITE HAS BEEN SUSPENDED"

    art = f"""
+--------------------------------------------------+
|  URL: {suspended_url}
|  STATUS: {notice}
+--------------------------------------------------+
"""
    slowprint("\nDisplaying suspended-site placeholder...\n")
    print(art)

    save = input("Save suspended-site note to 'suspended_links.txt'? (y/n): ").lower()
    if save == "y":
        with open("suspended_links.txt", "a") as f:
            f.write(f"{time.ctime()} - {suspended_url} - {notice}\n")
        print("Saved to suspended_links.txt")


# --------------------------- NETWORK REPORT ---------------------------

def generate_report(include_suspended=False):
    slowprint("\nGenerating diagnostic report...\n")

    hostname = socket.gethostname()
    local_ip = get_local_ip()

    try:
        google_ip = socket.gethostbyname("google.com")
    except:
        google_ip = "Unavailable"

    report_lines = [
        "==================== NETWORK REPORT ====================\n",
        f"Generated: {time.ctime()}\n",
        f"Hostname: {hostname}\n",
        f"Operating System: {platform.system()} {platform.release()}\n",
        f"Local IP: {local_ip}\n",
        f"DNS Test: google.com → {google_ip}\n",
        "\nSpeed Test (Simulated):\n",
        f"    Download: {round(random.uniform(20, 200), 2)} Mbps\n",
        f"    Upload: {round(random.uniform(5, 120), 2)} Mbps\n",
        f"    Ping: {round(random.uniform(5, 60), 2)} ms\n",
    ]

    if include_suspended:
        report_lines.append("\nSuspended Sites Found (placeholder):\n")
        report_lines.append(" - http://example-suspended-site.com  [SUSPENDED]\n")

    report = "".join(report_lines)
    print(report)

    with open("network_report.txt", "w") as f:
        f.write(report)

    print("📄 Report saved as: network_report.txt")


# --------------------------- MENU SYSTEM ---------------------------

def menu():
    print("""
===================== MENU =====================

1. Validate IP Address
2. Show Local Network Info
3. Ping Test
4. DNS Lookup
5. Run Speed Test
6. Generate Network Report
7. Show Suspended Site Example
8. Phone Number Checker / Telco Detector
0. Exit

================================================
""")
    return input("Choose an option: ")


# --------------------------- MAIN ---------------------------

def main():
    clear_screen()
    print_banner()
    slowprint("Initializing Supreme Network Tool...\n")

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
            inc = input("Include suspended-site placeholders? (y/n): ")
            generate_report(include_suspended=(inc.lower() == "y"))
        elif choice == "7":
            show_suspended_site_example()
        elif choice == "8":
            number_checker()
        elif choice == "0":
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

        input("\nPress ENTER to return to menu...")
        clear_screen()


if __name__ == "__main__":
    main()