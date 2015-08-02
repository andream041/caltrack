import serial
import datetime
import re

ser=serial.Serial('/dev/ttyUSB0', 9600)

curtime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
#print(curtime)
#x = ser.read(100)

#y = ser.readline()
#curtime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
#print('byte', y)
#print(curtime)


#weights = re.findall(b'[0-9\.]+', y)
#m = re.search(b'([\d\.]+) (a-z)+', y)
#m = re.search(b'([\d\.]+) ([a-z]+)',y)
#m = re.search(b'(?P<net_weight>[\d\.]+ ) (?P<net_weight_unit>[a-z:]+ ) ([\d\.]+ ).+([\d\.]+ )',y)
#m = re.search(b'(?P<display_weight>[\d\.]) +(?P<display_weight_unit>[a-z:]+).+(?P<net_weight>[\d\.]+ ).+(?P<gross_weight>[\d\.]+ )',y)
#print('long_match')
##if not m:
    ##m = re.search(b'(?P<net_weight>[\d\.]+)', y)
    ##print('short_match')
##print(m.group(0))
#print(m.groups())
##print('net weight', m.group('net_weight'))
#print('display weight', m.group('display_weight'))
#print('display weight_unit', m.group('display_weight_unit'))
#weight = y[0:9]
#unit = y[10:15]
#stability = y[16:17]
#print(unit)
#print(weight)

#r = y.split(b' ')

#print('x', x)
#print(ser.name)

try:
    while True:
        y = ser.readline()
        print('line', y)

        #assert not re.match(b' T', y)
        
        #isstable = (y.find(b'?') == -1)
        #print('stable', isstable)
        try:
            assert y.find(b'?') == -1
        except AssertionError:
            continue

        m = re.match(b' *(?P<net_weight>[-\d\.]+) +(?P<unit>[a-z:]+)[A-Z ]+(?P<gross_weight>[-\d\.]+) +(?P=unit)[A-Z ]+(?P<tare_weight>[-\d\.]+) (?P=unit)', y)
        if not m:
            m = re.match(b' *(?P<net_weight>[\d\.]+) +(?P<unit>[a-z:]+)', y)

        try:
            print(m.groups())
        except AttributeError:
            print('no match')
            continue
        #print(m.group('net_weight'))
        #print(m.group('unit'))
        #print(m.group('gross_weight'))
        #print(m.group('tare_weight'))
            
except KeyboardInterrupt:
        exit
ser.close()
