#!/usr/bin/env python3

#Imports for HID part
from time import sleep

#Imports for API part
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
from urllib.parse import urlparse
import json
import re

#Variables
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

values = {
'a':'write_report(NULL_CHAR*2 +chr(4)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'b':'write_report(NULL_CHAR*2 +chr(5)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'c':'write_report(NULL_CHAR*2 +chr(6)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'd':'write_report(NULL_CHAR*2 +chr(7)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'e':'write_report(NULL_CHAR*2 +chr(8)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'f':'write_report(NULL_CHAR*2 +chr(9)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'g':'write_report(NULL_CHAR*2 +chr(10)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'h':'write_report(NULL_CHAR*2 +chr(11)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'i':'write_report(NULL_CHAR*2 +chr(12)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'j':'write_report(NULL_CHAR*2 +chr(13)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'k':'write_report(NULL_CHAR*2 +chr(14)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'l':'write_report(NULL_CHAR*2 +chr(15)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'm':'write_report(NULL_CHAR*2 +chr(16)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'n':'write_report(NULL_CHAR*2 +chr(17)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'o':'write_report(NULL_CHAR*2 +chr(18)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'p':'write_report(NULL_CHAR*2 +chr(19)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'q':'write_report(NULL_CHAR*2 +chr(20)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'r':'write_report(NULL_CHAR*2 +chr(21)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
's':'write_report(NULL_CHAR*2 +chr(22)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
't':'write_report(NULL_CHAR*2 +chr(23)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'u':'write_report(NULL_CHAR*2 +chr(24)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'v':'write_report(NULL_CHAR*2 +chr(25)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'w':'write_report(NULL_CHAR*2 +chr(26)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'x':'write_report(NULL_CHAR*2 +chr(27)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'y':'write_report(NULL_CHAR*2 +chr(28)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'z':'write_report(NULL_CHAR*2 +chr(29)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'A':'write_report(chr(2)+NULL_CHAR+chr(4)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'B':'write_report(chr(2)+NULL_CHAR+chr(5)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'C':'write_report(chr(2)+NULL_CHAR+chr(6)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'D':'write_report(chr(2)+NULL_CHAR+chr(7)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'E':'write_report(chr(2)+NULL_CHAR+chr(8)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'F':'write_report(chr(2)+NULL_CHAR+chr(9)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'G':'write_report(chr(2)+NULL_CHAR+chr(10)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'H':'write_report(chr(2)+NULL_CHAR+chr(11)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'I':'write_report(chr(2)+NULL_CHAR+chr(12)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'J':'write_report(chr(2)+NULL_CHAR+chr(13)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'K':'write_report(chr(2)+NULL_CHAR+chr(14)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'L':'write_report(chr(2)+NULL_CHAR+chr(15)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'M':'write_report(chr(2)+NULL_CHAR+chr(16)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'N':'write_report(chr(2)+NULL_CHAR+chr(17)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'O':'write_report(chr(2)+NULL_CHAR+chr(18)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'P':'write_report(chr(2)+NULL_CHAR+chr(19)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'Q':'write_report(chr(2)+NULL_CHAR+chr(20)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'R':'write_report(chr(2)+NULL_CHAR+chr(21)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'S':'write_report(chr(2)+NULL_CHAR+chr(22)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'T':'write_report(chr(2)+NULL_CHAR+chr(23)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'U':'write_report(chr(2)+NULL_CHAR+chr(24)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'V':'write_report(chr(2)+NULL_CHAR+chr(25)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'W':'write_report(chr(2)+NULL_CHAR+chr(26)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'X':'write_report(chr(2)+NULL_CHAR+chr(27)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'Y':'write_report(chr(2)+NULL_CHAR+chr(28)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'Z':'write_report(chr(2)+NULL_CHAR+chr(29)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'1':'write_report(NULL_CHAR*2 +chr(30)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'2':'write_report(NULL_CHAR*2 +chr(31)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'3':'write_report(NULL_CHAR*2 +chr(32)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'4':'write_report(NULL_CHAR*2 +chr(33)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'5':'write_report(NULL_CHAR*2 +chr(34)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'6':'write_report(NULL_CHAR*2 +chr(35)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'7':'write_report(NULL_CHAR*2 +chr(36)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'8':'write_report(NULL_CHAR*2 +chr(37)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'9':'write_report(NULL_CHAR*2 +chr(38)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'0':'write_report(NULL_CHAR*2 +chr(39)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'!':'write_report(chr(2)+NULL_CHAR+chr(30)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'@':'write_report(chr(2)+NULL_CHAR+chr(31)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'#':'write_report(chr(2)+NULL_CHAR+chr(32)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'&':'write_report(chr(2)+NULL_CHAR+chr(36)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'*':'write_report(chr(2)+NULL_CHAR+chr(37)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'(':'write_report(chr(2)+NULL_CHAR+chr(38)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
')':'write_report(chr(2)+NULL_CHAR+chr(39)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'-':'write_report(NULL_CHAR*2 +chr(45)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'=':'write_report(NULL_CHAR*2 +chr(46)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'{':'write_report(NULL_CHAR*2 +chr(47)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'}':'write_report(NULL_CHAR*2 +chr(48)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'\\':'write_report(NULL_CHAR*2 +chr(49)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
';':'write_report(NULL_CHAR*2 +chr(51)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'':'write_report(NULL_CHAR*2 +chr(52)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'`':'write_report(NULL_CHAR*2 +chr(53)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
',':'write_report(NULL_CHAR*2 +chr(54)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'.':'write_report(NULL_CHAR*2 +chr(55)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'/':'write_report(NULL_CHAR*2 +chr(56)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'|':'write_report(chr(2)+NULL_CHAR+chr(50)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
':':'write_report(chr(2)+NULL_CHAR+chr(51)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'"':'write_report(chr(2)+NULL_CHAR+chr(52)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'<':'write_report(chr(2)+NULL_CHAR+chr(54)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'>':'write_report(chr(2)+NULL_CHAR+chr(55)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'?':'write_report(chr(2)+NULL_CHAR+chr(56)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'}':'write_report(NULL_CHAR*2 +chr(79)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'{':'write_report(NULL_CHAR*2 +chr(80)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
']':'write_report(chr(2)+NULL_CHAR+chr(79)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',
'[':'write_report(chr(2)+NULL_CHAR+chr(80)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)',

#Next Signs are used for different keymappings
'$':'write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #ENTER
'%':'write_report(NULL_CHAR*2 +chr(41)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #ESC
'^':'write_report(NULL_CHAR*2 +chr(42)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #BACKSPACE
'~':'write_report(NULL_CHAR*2 +chr(43)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #TAB
'_':'write_report(NULL_CHAR*2 +chr(44)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #SPATIE
'+':'write_report(NULL_CHAR*2 +chr(70)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #PRINT SCREEN
'[':'write_report(NULL_CHAR*2 +chr(76)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #DELETE
']':'write_report(chr(5)+NULL_CHAR+chr(76)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #CTRL+ALT+DEL
'|':'write_report(NULL_CHAR*2 +chr(81)+NULL_CHAR*5)\nwrite_report(NULL_CHAR * 8)', #DOWN
'^':'sleep(0.5)', #WAIT 0.5s
}

def writeToHID(user_input):
    #Create an empty list which we will fill later
    translated_list = []
        
    #FOR Loop, loops every letter trough dictionary and saves translation in             translated_list
    for letter in user_input:
       if letter in values:
           translated_list.append(values[letter])
    
    exec ("\n".join(translated_list))
    #End with a NULL command to release all keys and avoid a endless string
    write_report(NULL_CHAR * 8)

def unlockPC(password):
    print('Unlocking screen with given password')
    writeToHID(']^^' + password + '$');

def enterLoginPassword(login,password):
    print('Entering your password')
    writeToHID(login+'~'+password);

def enterPassword(password):
    print('Entering your password')
    writeToHID(password);

def lockPC():
    print('Locking screen')
    writeToHID(']^^$');

def inputFromUser():
    user_input = input(": ")
    print('[' + user_input + ']')
    if (user_input == 'lock and unlock'):
        p4ssw0rd = ''
        user_input = '^^^^]^^$^^^^^^^^^^^^^^^^^^^^^]^^' + p4ssw0rd + '$'

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
        return

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len).decode()
        data = json.loads(post_body)
        if(data["command"]=="unlockPC" and data["password"]!=""):
            unlockPC(data["password"])
        if(data["command"]=="enterLoginPassword" and data["password"]!="" and data["login"]!=""):
            enterLoginPassword(data["login"],data["password"])
        if(data["command"]=="enterPassword" and data["password"]!=""):
            enterPassword(data["password"])
        if(data["command"]=="lockPC"):
            lockPC()

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version,
            'body': data
        }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('', 8443), RequestHandler)
    server.socket = ssl.wrap_socket(server.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)
    print('Starting server at https://*:8443')
    server.serve_forever()
