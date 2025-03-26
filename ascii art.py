import os, time, sys
from colorama import Fore, Style, init, Back
init()

os.system("clear")

def intro():
    filenames = []
    frames = []
    for i in range(1, 11):
        filenames.append(f'ascii_art/animation{i}.txt')

    for name in filenames:
        with open(name, "r", encoding="utf-8") as f:
            frames.append(f.read())

    end_time = time.time() + 3
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write('\033[2J\033[H')
            sys.stdout.write(banner + frame)
            sys.stdout.flush()
            time.sleep(0.3)



CYAN = Fore.CYAN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

text = "By: Mitchell Zhou, Yunna Wang, Jeet Vijaywargi"
banner = f"""

   ██████╗  ███████╗ ███╗   ██╗     █████╗  ██╗  █████╗
  ██╔════╝  ██╔════╝ ████╗  ██║    ██╔══██╗ ██║ ██╔══██╗
  ██║  ███╗ █████╗   ██╔██╗ ██║    ███████║ ██║ ███████║
  ██║   ██║ ██╔══╝   ██║╚██╗██║    ██╔══██║ ██║ ██╔══██║
  ╚██████╔╝ ███████╗ ██║ ╚████║    ██║  ██║ ██║ ██║  ██║
   ╚═════╝  ╚══════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝
╔═══════════════════════════════════════════════════════╗
║{RED} Applied Information Assurance {RESET}| {CYAN}Tomcat_CVE-2025-24813{RESET} ║
╚═══════════════════════════════════════════════════════╝
   🕵️ {text} 👮
"""

intro()

