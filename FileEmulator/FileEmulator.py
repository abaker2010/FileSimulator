#!/usr/bin/python
# Wrote by: Aaron Baker

from classes.RepeatedTimer import RepeatedTimer
from classes.HttpRequestHandler import HttpRequestHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import urllib.request 
import colorama
from colorama import Fore, Back, Style


global Get_Count

# This is used for getting information from the server
def Get_From_Server():
    global Get_Count
    global GetFromServer
    print(Fore.LIGHTYELLOW_EX + "[+] Client Requesting: {%s}" % Get_Count)
    url = 'http://127.0.0.1:8085/index.html/'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8') 
    Get_Count += 1
    
    return
# This is used for setting up and starting the server
def StartServer():
    # Server settings
    server_address = ('127.0.0.1', 8085)
    httpd = HTTPServer(server_address, HttpRequestHandler)
    print(Fore.LIGHTGREEN_EX + 'running server...\n')
    Style.RESET_ALL
    Fore.YELLOW
    httpd.serve_forever()
    return

# Default main
def main():
    global GetFromServer
    global Serverthread
    global Get_Count
    Get_Count = 0
    colorama.init() 
    print(Fore.LIGHTRED_EX + "Starting server")
    Serverthread = threading.Thread(target=StartServer)

    Serverthread.setDaemon(True)
    Serverthread.start()

    GetFromServer = RepeatedTimer(1.5, Get_From_Server)

    while True:
        time.sleep(1000)
    return

# Exiting the console and stopping HTTP Server 
def exit_gracefully():
    global GetFromServer
    GetFromServer.stop()
    print("Stopping...")
    return

# Default main call
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        exit_gracefully();
