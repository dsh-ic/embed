import smbus2
import time


bus = smbus2.SMBus(1)
# SI7021 address, 0x40(64)

si_addr=0x40
define read_hum():
  rh = bus.read_i2c_block_data(si_addr, 0xE5, 2) 
# sends a 0xE5 command (measure RH, hold master mode) and read 2 bytes back
  time.sleep(0.1)
# Convert the data
  humidity = ((rh[0] * 256 + rh[1]) * 125 / 65536.0) - 6
  return humidty

define read_temp():
  # Read data , 2 bytes, Temperature MSB first
  temp = bus.read_i2c_block_data(si_addr, 0xE3,2)
#what really happens here is that master sends a 0xE3 command (measure temperature, hold master mode) and read 2 bytes back 
#if you read 3 bytes the last one is the CRC!
  time.sleep(0.1)

# Convert the data
  Temp = ((temp[0] * 256 + temp[1]) * 175.72 / 65536.0) - 46.85
  return Temp
#
