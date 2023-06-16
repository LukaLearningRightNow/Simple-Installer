import subprocess as sub
from rich.console import Console
import shutil
import wget
import random
import time
import yaml
import json
import os
import sys

rich_Console = Console()

SimpleInstallerCurrentPath = os.path.dirname(os.path.realpath(__file__))

installDir = SimpleInstallerCurrentPath + "\\downloads"


# Application


rich_Console.print("[green]Simple installer[/green] | 0.5 | ")

# User Input

UserCommandInput = input("# ")



# Commands

if UserCommandInput == 'install':
    rich_Console.print("Link: [blue](For Example github!<USERNAME>/<REPOSITORY_NAME>/<BRANCH>/<FILE>)[/blue]")
    UserInstallLinkInput = input("# ")
    if UserInstallLinkInput == "exit" or UserInstallLinkInput == "Exit" or UserInstallLinkInput == "EXIT":
        rich_Console.print("[red]Closing Application...[/red]")
        os.system("Simple_installer.exe")
        sys.exit()
    else:
        DownloadFiles = UserInstallLinkInput.replace("github!", "https://raw.githubusercontent.com/")
        rich_Console.print("[green]Installing Started...[/green]")
        DownloadedFile = wget.download(DownloadFiles, installDir)
        os.system(DownloadedFile)
        time.sleep(2)
        os.remove(DownloadedFile)
        rich_Console.print("\n[green]Successfully installed![/green]")
        time.sleep(3)
        os.system("Simple_installer.exe")
        sys.exit()


if UserCommandInput == "Help" or UserCommandInput == "help":
    rich_Console.print("[blue]What is This? This is Simple installer. With This You Can Install any github repository files easily or[/blue][red] any application/mods[/red]\n\n\n[green]--- List of Commands ---[/green]\nhelp - Prints out Help Page\ninstall - installs something\nexit - closing application\n")
    UserTempInput = input()
    os.system("Simple_installer.exe")
    sys.exit()


if UserCommandInput == "exit" or UserCommandInput == "Exit":
    rich_Console.print("[red]Closing...[/red]")
    time.sleep(2)
    sys.exit()



if UserCommandInput == "installget" or UserCommandInput == "installApp":
    rich_Console.print("Link: [blue](For Example github!<USERNAME>/<REPOSITORY_NAME>/<BRANCH>/<FILE_OR_DIR>)[/blue]")
    UserInstallLinkInput = input("# ")
    if UserInstallLinkInput == "exit" or UserInstallLinkInput == "Exit" or UserInstallLinkInput == "EXIT":
        rich_Console.print("[red]Closing Application...[/red]")
        os.system("Simple_installer.exe")
        sys.exit()
    else:
        DownloadFiles = UserInstallLinkInput.replace("github!", "https://raw.githubusercontent.com/")
        rich_Console.print("[green]Installing Started...[/green]")
        DownloadedFile = wget.download(DownloadFiles, installDir)
        time.sleep(2)
        rich_Console.print("\n[green]Successfully installed![/green]")
        time.sleep(3)
        os.system("Simple_installer.exe")
        sys.exit()







else:
    rich_Console.print("[red]Unknown Command[/red]")
    time.sleep(3)
    os.system("Simple_installer.exe")
    sys.exit()