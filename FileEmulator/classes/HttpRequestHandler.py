#!/usr/bin/python
# Wrote by: Aaron Baker

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import colorama
from colorama import Fore, Back, Style

# HTTPRequestHandler class
class HttpRequestHandler(BaseHTTPRequestHandler):

    def Load_Main_Page(self):
        Path = os.path.dirname(os.path.abspath(__file__))
        page = ""
        with open(Path + "\\..\\" + "\index.html", "r") as file:
            for line in file:
                page += line;
        return page
  # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send message back to client
        message = self.Load_Main_Page()
        returned = bytes(message, "utf8")
        print(Fore.LIGHTGREEN_EX + "[-] Server Sending Package\n" + Style.RESET_ALL)
        return