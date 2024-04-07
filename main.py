from RLY8Class import RLY8

ADDR = ("192.168.0.202", 2000)

rly8 = RLY8()

print(rly8.name)
print(rly8.netconf)
print(rly8.version)
print(rly8.baudrate)

# rly8.setName("DFRobot")
# rly8.setBaudrate(115200)

# print(rly8.name)
# print(rly8.netconf)
# print(rly8.version)
# print(rly8.baudrate)

rly8.setRelayStatus(1, "off")
print(rly8.relay1)

# print(rly8.getName)