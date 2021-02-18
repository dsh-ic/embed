#!/usr/bin/env python

from __future__ import division, print_function
from nxp_imu import IMU
import time
from bmp280 import bmp280_readata,bmp280_convert

"""
accel/mag - 0x1f
gyro - 0x21
pi@r2d2 nxp $ sudo i2cdetect -y 1
	0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 1f
20: -- 21 -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
"""

# the following function is able to read all the data from the sensor,but it not use in the main
def imu():
	imu = IMU(gs=4, dps=2000, verbose=True)
	header = 67
	print('-'*header)
	print("| {:17} | {:20} | {:20} |".format("Accels [g's]", " Magnet [uT]", "Gyros [dps]"))
	print('-'*header)
	for _ in range(10):
		a, m, g = imu.get()
		print('| {:>5.2f} {:>5.2f} {:>5.2f} | {:>6.1f} {:>6.1f} {:>6.1f} | {:>6.1f} {:>6.1f} {:>6.1f} |'.format(
			a[0], a[1], a[2],
			m[0], m[1], m[2],
			g[0], g[1], g[2])
		)
		time.sleep(0.50)
	print('-'*header)
	print(' uT: micro Tesla')
	print('  g: gravity')
	print('dps: degrees per second')
	print('')

#this function convert sensor data to roll,pitch and yaw. However,yaw is not accurate enough without use of kalman filter and
# other alogorithm such as sensor fusion. stepper motor may use instead
def ahrs():
	print('')
	imu = IMU(verbose=True)
	header = 47
	print('-'*header)
	print("| {:20} | {:20} |".format("Accels [g's]", "Orient(r,p,h) [deg]"))
	print('-'*header)
	fall = False
	#for _ in range(10):
	while True:
		a, m, g = imu.get()# get data from nxp-9dof fxos8700 + fxas21002
		r, p, h = imu.getOrientation(a, m) # convert sensor data to angle in roll,pitch,yaw axis
		#print the angle data
		#print('| {:>6.1f} {:>6.1f} {:>6.1f} | {:>6.1f} {:>6.1f} {:>6.1f} |'.format(a[0], a[1], a[2], r, p, h))
		time.sleep(1)

		r = abs(r)
		p = abs(p)
		#h =abs(h)

		if r>50 or p>50 :
			fall = True
		else:
			fall =False
		if fall:
			print("the flower pot is fall over")
		else:
			print("nothing wrong")



	#print('-'*header)
	#print('  r: roll')
	#print('  p: pitch')
	#print('  h: heading')
	#print('  g: gravity')
	#print('deg: degree')
	#print('')

if __name__ == "__main__":
	try:
		ahrs()
		#imu()
	except Exception as e:
		print(e)
	except KeyboardInterrupt:
		pass
	try:
		data=bmp280_readdata(0x77)
		p=bmp280_convert(data)
		print(p)
	except Exception as e:
		print(e)
	except KeyboardInterrupt:
		pass
	#print('Done ...'
