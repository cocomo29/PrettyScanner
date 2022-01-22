import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(0.01)


def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[-] Port {} is closed".format(port),"red"))
    else:
        print(colored("[+] Port {} is open".format(port), "green"))


host = input("[*] Enter the host to scan: ")
ask = input("Choose an option:\n1. Scan all ports\n2. Scan specific ports\n3. Exit\n")


if ask == "1":
    for port in range(1,63536):
        portscanner(port)
elif ask == "2":
    ports = input("Enter the ports separated by a comma: ")
    ports = str(ports).split(",")
    for port in ports:
        portscanner(int(port))
elif ask == "3":
    exit()
