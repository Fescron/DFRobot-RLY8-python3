# DFRobot RLY-8 Python 3 Control Class and Example Code

This repository contains a control class and other example code for the [RLY-8](https://www.dfrobot.com/product-1218.html) 8 channel PoE ethernet (and USB) relay controller by [DFRobot](https://www.dfrobot.com). See [this](https://wiki.dfrobot.com/RLY-8-POE_Relay_Controller_DFR0289) link to their wiki-page for more information about the device.

The code on this repository was originally written by Geréb Róbert in Python 2 (see [this](https://github.com/uponai/dfrobot-RLY-8-python) repository). I've ported it to Python 3 and added slightly more functionality and documentation.

<br>

## Repository Files

- `RLY8Class.py`: Control class for the relay
- `main.py`: A basic Python-file which uses the `RLY8Class.py` file to control the relay
- `rly-8.py`: Stand-alone example to control the relay

<br>

## `RLY8Class.py` usage

```python
from RLY8Class import RLY8

# Define the IP and port to connect to
# (DHCP is enabled by default, unfortunately the device doesn't have a hostname)
ADDR = ("192.168.0.202", 2000)

# Instantiate the RLY-8 object
rly8 = RLY8(ADDR)

# Print some information
print(rly8.name)
print(rly8.netconf)
print(rly8.version)
print(rly8.baudrate)

# Change some basic settings
rly8.setName("DFRobot2") # Default: "DFRobot"
rly8.setBaudrate(9600)   # Default: 115200

# Enable a relay (relays are numbered 1 to 8, states are "on" or "off")
rly8.setRelayStatus(1, "on")

# Print the status of a relay
print(rly8.relay1)
```
