#!/usr/bin/env python3

""" Network Diagnostic Checker with Suspended-Site Placeholder Author: ChatGPT Features:

IP validation

Local IP info

Ping test

DNS lookup

Simulated speed test

Generate network report (saves to file)

"Suspended site" placeholder / example (safe, cosmetic only)

Pure built-in modules (no requirements.txt) """


import os 
import subprocess 
import socket
import platform
import ipaddress 
import time
import random

--------------------------- Utilities ---------------------------

def clear_screen(): try: os.system('cls' if platform.system().lower() == 'windows' else 'clear') except: pass

def print_banner(): banner = r"""


---

| \ | | | |      _____  _ | | ___ |  | |/ _ \ \ \ /\ / / _ | '| |/ _ 
| |\  |  / | \ V  V / () | |  | |  __/ || _|_|__| _/_/ _/||  ||__| NETWORK & WIFI DIAGNOSTIC TOOL Developed by SupremeModzDev — Python Edition """ print(banner)

def slowprint(text, speed=0.005): for char in text: print(char, end="", flush=True) time.sleep(speed) print()

--------------------------- IP / Network Validators ---------------------------

def is_valid_ip(ip): try: ipaddress.ip_address(ip) return True except ValueError: return False

def validate_ip_menu(): ip = input("\nEnter IP to validate: ") if is_valid_ip(ip): print(f" ✔ VALID IP: {ip}") else: print(f" ✘ INVALID IP: {ip}")

--------------------------- Local Network Information ---------------------------

def get_local_ip(): try: s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) s.connect(("8.8.8.8", 80)) ip = s.getsockname()[0] s.close() return ip except: return None

def show_local_info(): slowprint("\nFetching local network information...") hostname = socket.gethostname() local_ip = get_local_ip()

print(f"\n 🖥 Hostname: {hostname}")
print(f" 📡 Local IP: {local_ip if local_ip else 'Unavailable'}")
print(f" 🧪 Platform: {platform.system()} {platform.release()}")

--------------------------- Ping Tester ---------------------------

def ping(host, count=4, timeout=4): # host may be hostname or ip param = "-n" if platform.system().lower() == "windows" else "-c" command = ["ping", param, str(count), host]

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

def ping_menu(): host = input("\nEnter IP/Host to ping: ") result = ping(host) print(result)

--------------------------- DNS Test ---------------------------

def dns_lookup(domain): try: slowprint("\nResolving DNS...") ip = socket.gethostbyname(domain) return f"{domain} → {ip}" except Exception as e: return f"DNS Error: {e}"

def dns_menu(): domain = input("\nEnter domain (example: google.com): ") print(dns_lookup(domain))

--------------------------- Simulated Speed Test ---------------------------

def simulate_speed_test(): slowprint("\nRunning safe simulated speed test...") for i in range(20): print("▉", end="", flush=True) time.sleep(0.05) print("\n")

download = round(random.uniform(20, 250), 2)
upload = round(random.uniform(5, 120), 2)
ping_ms = round(random.uniform(5, 60), 2)

return download, upload, ping_ms

def speed_test_menu(): down, up, latency = simulate_speed_test() print(f" 📥 Download Speed: {down} Mbps") print(f" 📤 Upload Speed: {up} Mbps") print(f" 🏓 Ping: {latency} ms")

--------------------------- Suspended Site Placeholder ---------------------------

def show_suspended_site_example(): """ This function prints a cosmetic "suspended site" example. It's purely aesthetic — used to simulate a disabled/suspended site entry in reports. Do NOT use for phishing or impersonation. """ suspended_url = "http://example-suspended-site.com" notice = "THIS SITE HAS BEEN SUSPENDED"

art = f"""

+--------------------------------------------------+ |  {suspended_url} |  {notice} +--------------------------------------------------+ """ slowprint("\nDisplaying suspended-site placeholder...\n") print(art)

# Optionally save to file for the report
save = input("Save suspended-site note to 'suspended_links.txt'? (y/n): ")
if save.strip().lower() == 'y':
    try:
        with open('suspended_links.txt', 'a') as f:
            f.write(f"{time.ctime()} - {suspended_url} - {notice}\n")
        print("Saved to suspended_links.txt")
    except Exception as e:
        print(f"Could not save: {e}")

--------------------------- Network Report ---------------------------

def generate_report(include_suspended=False): slowprint("\nGenerating diagnostic report...\n")

hostname = socket.gethostname()
local_ip = get_local_ip()

try:
    google_ip = socket.gethostbyname('google.com')
except:
    google_ip = 'Unavailable'

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
    # append suspended placeholder to report
    report_lines.append('\nSuspended Sites Found (placeholder):\n')
    report_lines.append(' - http://example-suspended-site.com  [SUSPENDED]\n')

report = ''.join(report_lines)
print(report)

try:
    with open('network_report.txt', 'w') as f:
        f.write(report)
    print("📄 Report saved as: network_report.txt")
except Exception as e:
    print(f"Could not save report: {e}")

--------------------------- Menu System ---------------------------

def menu(): print(""" ==================== MENU ====================

1. Validate IP Address


2. Show Local Network Info


3. Ping Test


4. DNS Lookup


5. Run Speed Test


6. Generate Network Report


7. Show Suspended Site Example (placeholder)


8. Exit """) return input("Choose an option: ")



--------------------------- Main Loop ---------------------------

def main(): clear_screen() print_banner() slowprint("Initializing Network Diagnostic Tool...\n")

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
        inc = input("Include suspended-site placeholders in report? (y/n): ")
        generate_report(include_suspended=(inc.strip().lower() == 'y'))
    elif choice == "7":
        show_suspended_site_example()
    elif choice == "0":
        print("\nExiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

    input("\nPress Enter to return to menu...")
    clear_screen()

if name == 'main': main()