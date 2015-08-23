import serial
import datetime
import re
import pandas as pd
import psycopg2


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


def get_resolution(unit):
    if unit == b'kg':
        resolution = 0.0002
    if unit == b'g':
        resolution = 0.2
    if unit == b'lb':
        resolution = 0.0005
    if unit == b'oz':
        resolution = 0.01
    return(resolution)


ser=serial.Serial('/dev/ttyUSB0', 9600)

conn = psycopg2.connect("dbname=caltrack user=andrea")
df = pd.DataFrame(columns=('time', 'net', 'gross', 'tare'))
row=0
net0=0
try:
    while True:
        scale = ser.readline()

        curtime = datetime.datetime.now().isoformat()
        #date = curtime.date().isoformat()
        #time = curtime.time().isoformat()
        print('line', scale)
        #assert not re.match(b' T', y)
        
        #isstable = (y.find(b'?') == -1)
        #print('stable', isstable)
        # ? indicates scale not stable.
        try:
            assert scale.find(b'?') == -1
        except AssertionError:
            continue

        m = re.match(b' *(?P<net>[-\d\.:]+) +(?P<unit>[a-z:]+)[A-Z ]+(?P<gross>[-\d\.]+) +(?P=unit)[A-Z ]+(?P<tare>[-\d\.]+) (?P=unit)', scale)
        if not m:
            m = re.match(b' *(?P<net>[\d\.:]+) +(?P<unit>[a-z:]+)', scale)
        try:
            #print(m.groups())
            # Resolution: Keeps stuff being put in the db if the readings are apart by less than 2.1* scale resolution.
            #resolution = get_resolution(m.group('unit'))
            try:
                net, gross, tare = map(float, [m.group(x) for x in ['net', 'gross', 'tare']])
            except IndexError:
                net = float(m.group('net'))
                grossdf = None
                taredf = None
                gross = 'Null'
                tare = 'Null'
            #print('net0', net0, 'net', net)
            #print(net)
            #if abs(net-net0) < 2.1*resolution:
                #continue
            #curtime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

            try:
                df.loc[row] = [curtime, net, gross, tare]
            except NameError:
                df.loc[row] = [curtime, net, grossdf, taredf]

            #print(df.loc[row])
            cur = conn.cursor()
            cmd =   "INSERT INTO scaletest (time, net, gross, tare) VALUES \
                    ('{0}', {1}, {2}, {3}) \
                    ;".format(curtime, net, gross, tare)
            #print(cmd)
            cur.execute(cmd)
            conn.commit()
            cur.close()

            row+=1
            net0=net
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
conn.close()
print(df)


