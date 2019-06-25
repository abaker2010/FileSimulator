#!/usr/bin/python
# Wrote by: Aaron Baker

from classes.RepeatedTimer import RepeatedTimer
from classes.HttpRequestHandler import HttpRequestHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import urllib.request # pip install

global Get_Count

def Get_From_Server():
    global Get_Count
    global GetFromServer
    url = 'http://127.0.0.1:8085/index.html/'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8') 
    Get_Count += 1
    print("[+] Client Requesting: {%s}\n" % Get_Count)
    return

def StartServer():
    # Server settings
    server_address = ('127.0.0.1', 8085)
    httpd = HTTPServer(server_address, HttpRequestHandler)
    print('running server...')
    httpd.serve_forever()
    return

def main():
    global GetFromServer
    global Serverthread
    global Get_Count
    Get_Count = 0

    print("Starting server")
    
    Serverthread = threading.Thread(target=StartServer)

    Serverthread.setDaemon(True)
    Serverthread.start()

    GetFromServer = RepeatedTimer(1.5, Get_From_Server)

    while True:
        time.sleep(1000)
    return

def exit_gracefully():
    global GetFromServer
    GetFromServer.stop()
    print("Stopping...")
    return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        exit_gracefully();
