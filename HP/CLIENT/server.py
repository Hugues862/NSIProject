
#    - https://github.com/techwithtim/Network-Game-Tutorial

#    python 'C:\Users\hugue\Desktop\CODE\VSCODE\NSIProject\HP\CLIENT/server.py'
#    cd 'C:\Users\hugue\Desktop\CODE\VSCODE\NSIProject\HP\CLIENT/'



import socket
from os import system, name 
from _thread import *
import sys
import pickle
from rich.console import Console
from rich.table import Column, Table
import time
console = Console()

import classes.players as classPlayers

server = '192.168.0.15'
port = 5555
playerConn = [[[None],[None]],[[None],[None]]]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
console.log("Server running")

players = [classPlayers.Player(430,250),classPlayers.Player(1100,250)]


def printConsole():
    clear()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Data", style="dim", width=12)
    table.add_column("Server")
    table.add_column("Player 1")
    table.add_column("Player 2")

    table.add_row(
        "IP", str(server),str(playerConn[0][0]),str(playerConn[1][0])
    )
    table.add_row(
        "PORT", str(port),str(playerConn[0][1]),str(playerConn[1][1])
    )
    postxt1 = str(players[0].rect.x)+" : "+str(players[0].rect.y)
    postxt2 = str(players[1].rect.x)+" : "+str(players[1].rect.y)
    table.add_row(
        "POS", " ",postxt1,postxt2
    )
    console.print(table)
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')     


def consoleupdate():
    while True:
        time.sleep(1)
        clear()
        printConsole()
start_new_thread(consoleupdate)

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048*1))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                """ print("Received: ", data)
                print("Sending : ", reply) """

            conn.sendall(pickle.dumps(reply))
        except:
            break

    if player == 1:
        playerConn[1] = [None,None] 
    else:
        playerConn[0] = [None,None]
    conn.close()
 
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    if currentPlayer == 0 :
            playerConn[0] = addr
    else:
            playerConn[1] = addr

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

