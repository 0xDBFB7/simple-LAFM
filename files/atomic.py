
from time import sleep
import serial
from math import fabs
import numpy as np
psu = serial.Serial('/dev/ttyS0',115200,timeout=1)
printer = serial.Serial('/dev/ttyblackprinter',250000,timeout=None) #reprap serial port, change the baud rate to your printer's

f = open("./test.csv",'w+')

printer_x_home = 108 #initial position
printer_y_home = 100 

printer_x_step = 0.03
printer_y_step = 0.03
printer_x_travel = 10 # how far do we go on the bed?
printer_y_travel = 10

printer_z = 5.39
printer_z_high = 6.2

x_offset = 0

total_buffer = []

print('Homing Printer')
printer.write(b"G00 Z" + str(printer_z_high) + "\n")
sleep(5)
printer.write(b"G28\n")
printer.readline()
sleep(5)
print('Raising Printer')
printer.write(b"G00 Z" + str(printer_z_high) + "\n")
printer.readline()
sleep(10)
calibrate = 0
while not calibrate:
	try:
		psu.write("val1?\r\n")
		calibrate = float(psu.readline())
	except:
		pass

printer.write(b"G00 X" + str(printer_x_home) +" Y"+str(printer_y_home)+' F5000\n')
sleep(10)
for printer_x in np.arange(printer_x_home, printer_x_home+printer_x_travel, printer_x_step):
	for printer_y in np.arange(printer_y_home, printer_y_home+printer_y_travel, printer_y_step):
		printer.reset_input_buffer()
		printer.write(b"G00 X" + str(printer_x) +" Y"+str(printer_y)+'Z' + str(printer_z) +' F3000\n')
		sleep(0.7)
		current = 0
		while not current:
			try:
				psu.write("val1?\r\n")
				current = float(psu.readline())
			except:
				pass
		print(current)
		print(printer_x)
		print(printer_y)
		f.write(str(printer_x) + "," + str(printer_y) + "," + str(current-calibrate)+'\n')
	printer.write(b"G00 Z" + str(printer_z_high) + "\n")
	sleep(3)
	calibrate = 0
	while not calibrate:
		try:
			psu.write("val1?\r\n")
			calibrate = float(psu.readline())
			print('cal:')
			print(calibrate)
		except:
			pass
