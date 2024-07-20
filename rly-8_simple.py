import sys
import re
import socket
from time import sleep

ADDR = ("192.168.0.202", 2000)


total_arguments = len(sys.argv)
regex = re.compile(r"(?P<relay>\d)=(?P<state>.*)")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1) # [seconds]
s.connect(ADDR)

try:
    for i in range(1, total_arguments):
        result = regex.search(sys.argv[i])
        if result.group("relay") > "0" and result.group("relay") < "9":
            if result.group("state") in ["on", "On", "true", "True", "1"]:
                s.sendall((f'{{"relay{result.group("relay")}": "on"}}').encode())
            elif result.group("state") in ["off", "Off", "false", "False", "0"]:
                s.sendall((f'{{"relay{result.group("relay")}": "off"}}').encode())
            else:
                print("ERROR: Invalid syntax: '<relay(1-8)>=<state(on|On|true|True|1|off|Off|false|False|0)>'")
        else:
            print("ERROR: Invalid syntax: '<relay(1-8)>=<state(on|On|true|True|1|off|Off|false|False|0)>'")
        sleep(0.01)
except:
    print("ERROR: Exception")
    s.close()
