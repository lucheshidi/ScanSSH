import time
import os

def main():
    ipstr: str = input("Enter the IP address: ")
    try:
        ip: int = ipstr.split(".")
    except ValueError:
        print("Invalid IP address format. Please enter a valid IP address.")
        time.sleep(0.25)
        return
    if os.system(f"ssh {ipstr}") == 0:
        print("SSH connection closed.")
        flag = input("Do you want to connect another ip? (y/N): ").lower()
        if flag == "y":
            main()
        else:
            print("Exiting...")
            exit(0)

if __name__ == "__main__":
    main()