import nmap

scanner = nmap.PortScanner()

print("Welcome to gbScanner")
print("<------------------->")

ip = input("Insert the IP to be checked: ")
print("The IP is: ", ip)
type(ip)

menu = input("""\nChoose the type of scan:
                1 -> SYN scan  
                2 -> UDP scan
                3 -> Intense scan
                Type the chosen option: """)

print("The chosen option was:", menu)

if menu == "1":
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip, "1-1024", "-v -sS")
    print(scanner.scaninfo())
    print("IP status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Open doors:", scanner[ip]["tcp"].keys())

elif menu == "2":
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip, "1-1024", "-v -sU")
    print(scanner.scaninfo())
    print("IP status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Open doors:", scanner[ip]["udp"].keys())

elif menu == "3":
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip, "1-1024", "-v -sC")
    print("IP status:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Open doors:", scanner[ip]["tcp"].keys())

else:
    print("Choose a valid option!!!")