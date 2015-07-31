import serial
import datetime

ser=serial.Serial('/dev/ttyUSB0', 9600)

curtime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
print(curtime)
#x = ser.read(100)
curtime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
print(curtime)
#print('x', x)
#print(ser.name)
while True:
    line = ser.readline()
    print('line', line)
ser.close()
