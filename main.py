import subprocess
import time
import platform
import os

def exec(command: str):
    result: str = subprocess.run(
        command, shell=True, check=True, capture_output=True, text=True
    ).stdout.strip()
    return result

def get_os_name() -> str:
    os_name = platform.system().lower()
    if os_name == "linux":
        return "linux"
    elif os_name == "darwin":
        return "mac"
    elif os_name == "windows":
        return "Windows"
    else:
        print(f"Unsupported OS: {os_name}")
        time.sleep(0.25)
        return None

def init() -> None:
    global yellow, red, green, blue, reset
    yellow = "\033[93m"
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"
    reset = "\033[0m"

def main():
    init()
    if get_os_name() == "linux":
        print(f"Starting Linux script... ")
        time.sleep(3)


        print(f"""
        {green}------------------------------------------------------------------{reset}
        {green}Select what you want to do:{reset}
        {yellow}1. {blue}Scan a network segment for devices with OpenSSH Server installed and print out{reset}
        {yellow}2. {blue}Scan a device for OpenSSH Server installed and print out{reset}
        {yellow}3. {blue}Scan all the device in the network with OpenSSH Server installed and print out{reset}
        {green}------------------------------------------------------------------{reset}
        {yellow}4. {blue}add a device's ip address to the ips group{reset}
        {yellow}5. {blue}list the device in the ips group{reset}
        {yellow}6. {blue}remove a device's ip address from the ips group{reset}
        {green}------------------------------------------------------------------{reset}
        {yellow}7. try to connect a device in the ips group{reset}
        {green}------------------------------------------------------------------{reset}
        {green}8. {blue}Show the license of ScanSSH{reset}
        {green}0. {blue}Exit ScanSSH{reset}
        """)
        try:
            ip: int = input(f"{yellow}Enter here: {reset}")
        except ValueError:
            print(f"{red}Invalid input. Please enter a number.{reset}")
            time.sleep(0.25)
            raise SystemExit


        if os.system("mkdir ~/.scanssh/") == 0:
            open(f"~/.scanssh/ips.list", "w").close()
        elif os.system("mkdir ~/.scanssh/") == 1:
            global ips_list
            ips_list = open(f"~/.scanssh/ips.list", "w")
    elif get_os_name() == "windows":
        print(f"Starting Windows script... ")
        time.sleep(3)

        
        print(f"""
        {green}------------------------------------------------------------------{reset}
        {green}Select what you want to do:{reset}
        {yellow}1. {blue}Scan a network segment for devices with OpenSSH Server installed and print out{reset}
        {yellow}2. {blue}Scan a device for OpenSSH Server installed and print out{reset}
        {yellow}3. {blue}Scan all the device in the network with OpenSSH Server installed and print out{reset}
        {green}------------------------------------------------------------------{reset}
        {yellow}4. {blue}add a device's ip address to the ips group{reset}
        {yellow}5. {blue}list the device in the ips group{reset}
        {yellow}6. {blue}remove a device's ip address from the ips group{reset}
        {green}------------------------------------------------------------------{reset}
        {yellow}7. try to connect a device in the ips group{reset}
        {yellow}8. try to connect a device with IP{reset}
        {green}------------------------------------------------------------------{reset}
        {green}9. {blue}Show the license of ScanSSH{reset}
        {green}0. {blue}Exit ScanSSH{reset}
        """)
        try:
            ip: int = input(f"{yellow}Enter here: {reset}")
        except ValueError:
            print(f"{red}Invalid input. Please enter a number.{reset}")
            time.sleep(0.25)
            raise SystemExit
        

        if os.system("mkdir %USERPROFILE%\\.scanssh\\") == 0:
            open(f"%USERPROFILE%\\.scanssh\\ips.list", "w").close()
        elif os.system("mkdir %USERPROFILE%\\.scanssh\\") == 1:
            global ips_list
            ips_list = open(f"%USERPROFILE%\\.scanssh\\ips.list", "w")




if __name__ == "__main__":
    main()