import smbus2
import time


bus = smbus2.SMBus(1)
# SI7021 address, 0x40(64)

si_addr=0x40
