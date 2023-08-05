import os
import subprocess

from sys import executable
from pystyle import Colorate, Colors


def header() -> str:
    head = """                                                                                               
                .:-=+**####**+=-:.                
            :=*%@@@@@@@@@@@@@@@@@@%*=:            
         -*%@@@@@@@@@@@@@@@@@@@@@@@@@@%*-         
      .+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.      
     +@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@+     
   :%@@@@@@=  .:=#@@%%######%%@@#=:.  =@@@@@@%:   
  =@@@@@@@@.                          .@@@@@@@@=  
 -@@@@@@@@@-                          -@@@@@@@@@- 
:%@@@@@@@@+                            +@@@@@@@@%:
*@@@@@@@@+                              +@@@@@@@@*
@@@@@@@@@.                              .@@@@@@@@@
@@@@@@@@@.                              .@@@@@@@@@
@@@@@@@@@-                              -@@@@@@@@@
*@@@@@@@@%.                            .%@@@@@@@@*
:@@@@@@@@@%-                          -%@@@@@@@@@:
 =@@@@@%@@@@%=:                    :+%@@@@@@@@@@= 
  =@@@@=..=%@@@@%#*=          =*#%@@@@@@@@@@@@@=  
   :%@@@@+ .*@@@@@%:          :@@@@@@@@@@@@@@%:   
     +@@@@*   ::::             #@@@@@@@@@@@@+     
      .+@@@@*=----:            #@@@@@@@@@@+.      
         -#@@@@@@@#            #@@@@@@@#-         
            :+#%@@#            #@@%#+:            
                                                                                               
    """

    return Colorate.Horizontal(Colors.white_to_green, head)


def normal_prefix(message: str) -> str:
    prefix: str = Colors.gray + "[" + Colors.cyan + "»" + Colors.gray + "]" + Colors.dark_gray + " - "

    return prefix + Colors.white + message + Colors.reset


def error_prefix(message: str) -> str:
    prefix: str = Colors.gray + "[" + Colors.red + "X" + Colors.gray + "]" + Colors.dark_gray + " - "

    return prefix + Colors.red + message + Colors.reset


def success_prefix(message: str) -> str:
    prefix: str = Colors.gray + "[" + Colors.green + "✔" + Colors.gray + "]" + Colors.dark_gray + " - "

    return prefix + Colors.green + message + Colors.reset


def input_user() -> int | str:
    print(header())

    options: str = "1. Follow - 2. Unfollow - 3. Quit"

    try:
        print(Colorate.Horizontal(Colors.cyan_to_green, options))
        status = int(input(normal_prefix("")))

        if status == 3:
            exit(0)

        return status
    except ValueError:
        clear()
        return ""


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def install_dependencies() -> None:
    try:
        import pystyle
        import requests
        import discord
    except ModuleNotFoundError:
        try:
            subprocess.check_call([executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        except subprocess.CalledProcessError as e:
            print(f"Error during dependency installation: {e}")
