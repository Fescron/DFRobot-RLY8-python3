# DFRobot Python 3 Control Class and Example Code

The code was originally written by Geréb Róbert in Python 2, see [this](https://github.com/uponai/dfrobot-RLY-8-python) repository.

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
