import socket
import time
import json
ADDR = ("192.168.0.202", 2000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1) # Set the timeout to 1 second
s.connect(ADDR)

# get name
s.sendall(b'{"get":"name"}')
data = s.recv(1024).decode().split('\x00', 1)[0]
name = json.loads(data)['name']

# get netconfig
s.sendall(b'{"get":"netconfig"}')
data = s.recv(1024).decode().split('\x00', 1)[0]
netconf = json.loads(data)

# get version
s.sendall(b'{"get":"version"}')
data = s.recv(1024).decode().split('\x00', 1)[0]
version = json.loads(data)['version']

# get baudrate
s.sendall(b'{"get":"baudrate"}')
data = s.recv(1024).decode().split('\x00', 1)[0]
baudrate = json.loads(data)['baudrate']

relay_nr = 0
status = 'on'
try:
    while True:
        relay_nr += 1
        if relay_nr == 9:
            relay_nr = 1
            if status == 'on':
                status = 'off'
            else:
                status = 'on'
        s.sendall((f'{{"relay{relay_nr}": "{status}"}}').encode())
        data = s.recv(1024).decode().split('\x00', 1)[0]
        json_data = json.loads(data)
        # create final json version
        json_data['relay'] = relay_nr
        json_data['status'] = status
        json_data['name'] = name
        json_data['netconf'] = netconf
        json_data['version'] = version
        json_data['baudrate'] = baudrate
        print(json.dumps(json_data, indent=2))
        time.sleep(1)
except:
    s.close()
