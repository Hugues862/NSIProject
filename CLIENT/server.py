
#    - https://github.com/techwithtim/Network-Game-Tutorial

#    python 'C:\Users\hugue\Desktop\CODE\VSCODE\NSIProject\HP\CLIENT/server.py'
#    cd 'C:\Users\hugue\Desktop\CODE\VSCODE\NSIProject\HP\CLIENT/'


import classes.players as classPlayers
import socket
from os import system, name
import threading
import sys
import pickle
from rich.console import Console
from rich.table import Column, Table
import time
import datetime
import stages as stages

console = Console()


"""     Variables   """

consoleStatus = True
TransferBytes = 1024*2
fps = 60

"""-----------------"""
hostname = socket.gethostname()
#ipv4 = "192.168.1.41"
ipv4 = socket.gethostbyname(hostname)  # recupers l'adresse IP local
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ipv4
port = 5555
playerConn = [[["undef"], ["undef"]], [["undef"], ["undef"]]]
disconnect = [True, True]

win = None


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()


players = []
Stages = stages.initStages()


def printConsole():
    clear()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Users", style="dim", width=12)
    table.add_column("IP")
    table.add_column('PORT')
    table.add_row("Server", ipv4, str(port))
    for i in range(len(players)):
        try:
            table.add_row(f"Player {i}", str(
                Users[i][0][0]), str(Users[i][0][1]))
        except:
            pass
    console.print(table)
    """ 
    if disconnect[0]:
        ip1 = None
        port1 = None
    else:
        ip1 = str(playerConn[0][0])
        port1 = str(playerConn[0][1])

    if disconnect[1]:
        ip2 = None
        port2 = None
    else:
        ip2 = str(playerConn[1][0])
        port2 = str(playerConn[1][1])

    table.add_row(
        "IP", str(server),ip1,ip2
    )
    table.add_row(
        "PORT", str(port),port1,port2
    )
    postxt1 = str(players[0].rect.x)+" : "+str(players[0].rect.y)
    postxt2 = str(players[1].rect.x)+" : "+str(players[1].rect.y)
    table.add_row(
        "POS", " ",postxt1,postxt2
    ) """


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
console.log("Server running")


def consoleupdate():
    while True:
        time.sleep(1)
        clear()
        printConsole()


def gettime():
    dt = datetime.datetime.now()
    ms = str(dt.microsecond)
    return dt.strftime("%H:%M:%S:") + ms[2:]


if consoleStatus:
    ConsoleThread = threading.Thread(
        group=None, target=consoleupdate, name="ConsoleUpdate", args=(), kwargs={})
    ConsoleThread.start()

Users = []


def UpdatePlayerData(data, id):
    for name in data:
        global players
        if name == 'jump' and data[name] == True:

            if players[id].status["sleep"] == True:
                players[id].status["sleepSpam"] += 1

            else:
                players[id].jump()

        else:
            players[id].setAttribute(name, data[name])


def UpdatePlayers(id):
    players[id].update(Stages[0], fps)


def threaded_client(conn, id):
    # Connection started

    conn.send(pickle.dumps(id))
    conn.send(pickle.dumps(Stages))
    global players

    # main connection loop
    while True:
        try:
            #print(f"{gettime()} : data sent -> {players}")
            conn.send(pickle.dumps(players))
            data = pickle.loads(conn.recv(TransferBytes))
            #print(f"{gettime()} : data recieved -> {data}")
            UpdatePlayerData(data, id)
            UpdatePlayers(id)
        except:
            break

    # connection ends
    Users[id] == None
    players[id] == None
    conn.close()


""" 
    if player == 1:
        disconnect[1] = True 
    else:
        disconnect[0] = True
     """


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    #id = int(''.join(str(e) for e in [randint(0,9) for x in range(6)]))
    id = len(Users) + 0
    Users.append([addr, id])
    players.append(classPlayers.Player(430, 250, fps))
    thread = threading.Thread(
        group=None, target=threaded_client, name=f"Player{id}", args=(conn, id), kwargs={})
    thread.start()
