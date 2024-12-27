import generalDefs as methods
import bcrypt
import time
import re
import rich
import json
import uuid
import subprocess

methods.clear()
methods.printLine()

with open("manageUsers/users.json", 'r') as file:
    try:
        users = json.load(file)
    except json.JSONDecodeError:
        users = []


def checkuserValidation(usertocheck, passwordtocheck):
    for user in users:
        stored_pass = user["password"].encode('utf-8')
        if (user["username"] == usertocheck):
            if (bcrypt.checkpw(passwordtocheck.encode('utf-8'), stored_pass)):
                if (isloggedin() == usertocheck):
                    rich.print(
                        f"\n[red][bold]You can't play as both players [purple][italic]{username}![/italic][/purple] , you are already logged in as the Player1\n")
                    return False
                user["isPlayer2"] = True
                savejson(users)
                return True
            rich.print("[bold][red]Password is incorrect , Try again [/red][/bold]")
            return False
    rich.print("[bold][red]Username doesn't exists , Try again [/red][/bold]")
    return False


def allNotplayer2(users):
    for user in users:
        user["isPlayer2"] = False
    savejson(users)


def savejson(users):
    with open("manageUsers/users.json", 'w') as userjson:
        json.dump(users, userjson, indent=4)


def isloggedin():
    for user in users:
        if (user["isloggedin"] == True):
            return user["username"]
    return False


allNotplayer2(users)
if (isloggedin() == False):
    rich.print("[red][bold]You need to log in to be able to start a game! You're being redirected back to menu")
    time.sleep(2)
    subprocess.run(["python", "menu.py"], check=True)
for user in users:
    if (user["isloggedin"] == True):
        usrname = user["username"]
        rich.print(f"[purple][bold]Hello [italic][blue]{usrname}![/italic][/blue] [/purple][/bold]\n")
        rich.print(f"[yellow][italic]To start a game , log in as the Player2 :\n")
while (True):
    rich.print("[blue][bold]Enter your username :")
    username = input()
    rich.print("[blue][bold]Enter your password :")
    password = input()
    if (checkuserValidation(username, password)):
        time.sleep(0.5)
        rich.print(
            f"\n[purple][bold][blue][italic]{isloggedin()}[/blue][/italic] is playing as [italic][violet]Player1[/italic][/violet]")
        time.sleep(1)
        rich.print(f"\n[purple][bold][blue][italic]{username}[/blue][/italic] is playing as [italic][violet]Player2")
        time.sleep(1)
        rich.print("\n[green][bold]All set! Match is gonna start soon")
        time.sleep(2)
        rich.print("\n[white][bold]Match is Starting.")
        time.sleep(1)
        rich.print("[white][bold]Match is Starting..")
        time.sleep(1)
        rich.print("[white][bold]Match is Starting...")
        time.sleep(1)
        subprocess.run(["python", "coreGameplay/game.py"], check=True)
        break
