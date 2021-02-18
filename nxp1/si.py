import smbus2
import time

bus = smbus2.SMBus(1)

define shidu():
  rh = bus.read_i2c_block_data(si_addr, 0xE5, 2) 
# sends a 0xE5 command (measure RH, hold master mode) and read 2 bytes back
  time.sleep(0.1)
# Convert the data
  humidity = ((rh[0] * 256 + rh[1]) * 125 / 65536.0) - 6
  return humidty

 
